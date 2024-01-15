from django.urls import path
from .views import produit_list, produit_create, produit_update, produit_delete
from .views import categorie_create, categorie_list, categorie_delete, categorie_update
from .views import produits_par_categorie

urlpatterns = [
    path('produit/', produit_list, name='produit_list'),
    path('new/', produit_create, name='produit_new'),
    path('produit/edit/<int:pk>/', produit_update, name='produit_edit'),
    path('categorie/edit/<int:pk>/', categorie_update, name='categorie_edit'),
    path('produit/delete/<int:pk>/', produit_delete, name='produit_delete'),
    path('categorie/delete/<int:pk>/', categorie_delete, name='categorie_delete'),
    path('categorie/new/', categorie_create, name='categorie_new'),
    path('categorie/', categorie_list, name='categorie_list'),
    path('categorie/<int:pk>/produits/', produits_par_categorie, name='produits_par_categorie'),
]