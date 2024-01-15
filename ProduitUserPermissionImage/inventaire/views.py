from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Categorie
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

def categorie_create(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit_new')  # Redirige vers la page de création de produit après avoir ajouté une catégorie
    else:
        form = CategorieForm()
    return render(request, 'categorie/categorie_form.html', {'categorie_form': form})

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

# Delete
def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit_list')
    return render(request, 'produit/produit_confirm_delete.html', {'object': produit})

def categorie_delete(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('categorie_list')
    return render(request, 'categorie/categorie_confirm_delete.html', {'object': categorie})

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

def categorie_list(request):
	categorie = Categorie.objects.all()
	data = {'categorie' : categorie}
	return render(request, 'categorie/categorie_list.html', data)

def produits_par_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    produits = Produit.objects.filter(categorie=categorie)
    return render(request, 'categorie/categorie_produit_list.html', {'categorie': categorie, 'produits': produits})
