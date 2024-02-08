from django.contrib import admin
from .models import Produit, Categorie

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'code', 'quantite_stock', 'quantite_alerte', 'stock_securite')
    list_filter = ('categorie',) #Permet de filtrer par certaines catégories directement depuis l'interface d'administration.
    search_fields = ['nom', 'code']
    ordering = ('-quantite_stock',) #Ordonne les produits dans la liste; ici par quantité de stock décroissante.
    list_editable = ('quantite_stock', 'quantite_alerte', 'stock_securite')#Permet de modifier certains champs directement depuis la liste sans avoir à entrer dans le détail de l'objet.
    
        
admin.site.register(Produit, ProduitAdmin)
