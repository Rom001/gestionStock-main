from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserForm
from django.views import generic
from .models import CustomUser
from django.contrib.auth.decorators import user_passes_test

def admin_check(user):
    return user.is_superuser



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@user_passes_test(admin_check)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})

@user_passes_test(admin_check)
def user_create(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'user_form.html', {'form': form})

@user_passes_test(admin_check)
def user_update(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'admin/user_form.html', {'form': form})

@user_passes_test(admin_check)
def user_delete(request, pk):
    CustomUser.objects.get(pk=pk).delete()
    return redirect('user_list')