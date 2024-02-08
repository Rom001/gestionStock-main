from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorie
from .forms import CategorieForm
from django.db.models import Q
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

def categorie_create(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit_new')  # Redirige vers la page de création de produit après avoir ajouté une catégorie
    else:
        form = CategorieForm()
    return render(request, 'categorie/categorie_form.html', {'categorie_form': form})

def categorie_update(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)

    if request.method == 'POST':
        categorie_form = CategorieForm(request.POST, instance=categorie)    

        if categorie_form.is_valid():
            categorie = categorie_form.save(commit=False)
            categorie.save()        
            return redirect(reverse('categorie_list'))  # Redirection vers les détails du produit
                                     
    else:
        categorie_form = CategorieForm(instance=categorie)

    return render(request, 'categorie/categorie_form.html', {'categorie_form': categorie_form})

def categorie_delete(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('categorie_list')
    return render(request, 'categorie/categorie_confirm_delete.html', {'object': categorie})

def categorie_list(request):
	categorie = Categorie.objects.all()
	data = {'categorie' : categorie}
	return render(request, 'categorie/categorie_list.html', data)
