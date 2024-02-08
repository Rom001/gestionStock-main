from django.db import models
from categories.models import Categorie

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    quantite_stock = models.IntegerField()
    quantite_alerte = models.IntegerField()
    stock_securite = models.IntegerField()
                                            
    def __str__(self):
        return self.nom
    
class Image(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    
class EntreeStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # Autres champs pertinents ...

class SortieStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)