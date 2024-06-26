"""
URL configuration for bibliothèque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livres import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('livre/<int:livre_id>/', views.livre, name='livre'),
    path('ajouter/', views.ajout_livre, name='ajout_livre'),
    path('voir-livre/<int:livre_id>/', views.voir_livre, name='voir_livre'),
    path('livre/<int:livre_id>/modifier/', views.modifier_livre, name='modifier_livre'),
    path('supprimer/<int:livre_id>/', views.supprimer_livre, name='supprimer_livre'),
]
