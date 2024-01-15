
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static  # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gestion/', include('inventaire.urls')),  # Inclure les URL de l'application de gestion de produits
    path('users/', include('users.urls')),
    path("accounts/", include("django.contrib.auth.urls")), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

