from django.urls import path
from .views import produit_list, produit_create, produit_update, produit_delete
from .views import produits_par_categorie

urlpatterns = [
    path('', produit_list, name='produit_list'),
    path('new/', produit_create, name='produit_new'),
    path('edit/<int:pk>/', produit_update, name='produit_edit'),
    path('delete/<int:pk>/', produit_delete, name='produit_delete'),
    path('<int:pk>/produits/', produits_par_categorie, name='produits_par_categorie'),
]