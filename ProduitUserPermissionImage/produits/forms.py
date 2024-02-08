from django import forms
from .models import Produit, Categorie, Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['categorie', 'nom', 'code', 'quantite_stock', 'quantite_alerte', 'stock_securite']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'description']