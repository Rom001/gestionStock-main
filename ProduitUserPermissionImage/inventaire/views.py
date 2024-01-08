from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import CategorieForm, ProduitForm, ImageForm
from django.db.models import Q
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

# Create

def produit_create(request):
    if request.method == 'POST':
        produit_form = ProduitForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        
        if produit_form.is_valid() and image_form.is_valid():
            produit = produit_form.save(commit=False)
            produit.save()  # Maintenant, sauvegardez le produit

            image = image_form.save(commit=False)
            image.produit = produit
            image.save();           

            return redirect('produit_list')
    else:
        produit_form = ProduitForm()
        image_form = ImageForm()
    return render(request, 'produit/produit_form.html',  {'produit_form': produit_form, 'image_form': image_form} )

# Read
@login_required
def produit_list(request):
    query = request.GET.get('q')
    if query:
        produits = Produit.objects.filter(
            Q(nom__icontains=query) | 
            Q(code__icontains=query) |
            Q(categorie__nom__icontains=query)
        )
    else:
        produits = Produit.objects.all()
        
    context = {
        'produits': produits,
    }    
    return render(request, 'produit/produit_list.html', context)

# Update
def produit_update(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == 'POST':
        produit_form = ProduitForm(request.POST, instance=produit)
        image_form = ImageForm(request.POST, request.FILES, instance=produit.image if hasattr(produit, 'image') else None)
        

        if produit_form.is_valid() and (not hasattr(produit, 'image') or image_form.is_valid()):
            produit = produit_form.save(commit=False)
            produit.save()

            if hasattr(produit, 'image'):
                image = image_form.save(commit=False)
                image.produit = produit  # Association à nouveau si nécessaire
                image.save()
            else: # Si le produit n'a pas d'image, on en crée une nouvelle
                # On spécifie l'instance du produit comme paramètre
                image = image_form.save(commit=False)
                image.produit = produit
                image.save();           


            return redirect(reverse('produit_list'))  # Redirection vers les détails du produit
                                     
    else:
        produit_form = ProduitForm(instance=produit)
        image_form = ImageForm(instance=produit.image if hasattr(produit, 'image') else None)

    return render(request, 'produit/produit_form.html', {'produit_form': produit_form, 'image_form': image_form})

# Delete
def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit_list')
    return render(request, 'produit/produit_confirm_delete.html', {'object': produit})

def categorie_create(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit_new')  # Redirige vers la page de création de produit après avoir ajouté une catégorie
    else:
        form = CategorieForm()
    return render(request, 'categorie/categorie_form.html', {'form': form})