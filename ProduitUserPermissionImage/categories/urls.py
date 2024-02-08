from django.urls import path
from .views import categorie_create, categorie_list, categorie_delete, categorie_update

urlpatterns = [
    path('edit/<int:pk>/', categorie_update, name='categorie_edit'),
    path('delete/<int:pk>/', categorie_delete, name='categorie_delete'),
    path('new/', categorie_create, name='categorie_new'),
    path('', categorie_list, name='categorie_list'),
]