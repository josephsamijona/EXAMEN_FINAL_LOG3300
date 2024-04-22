from django.shortcuts import render, redirect
from livres.models import Livres
from .forms import LivreForm


# on ajoute les methodes pour les urls afin que le render des pages html puisse se faire 
# Create your views here.
def home(request):
   livres = Livres.objects.all()
   return render(request, 'index.html', {'livres': livres})

def livre(request ):
    # Logique pour récupérer les détails d'un livre spécifique en fonction de son ID
 
    return render(request, 'livre.html', {'livre': livre})

def ajout_livre(request):
    if request.method == 'POST':
        # Créer une instance de LivreForm avec les données de la requête POST
        form = LivreForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger l'utilisateur vers une autre page (par exemple, la liste des livres)
            return redirect('home')
    else:
        # Si la requête n'est pas de type POST, afficher un formulaire vide
        form = LivreForm()
    # Rendre le template avec le formulaire
    return render(request, 'ajoutlivre.html', {'form': form})

def modifier_livre(request ):
    # Logique pour afficher le formulaire pour modifier les informations d'un livre existant
 
    return render(request, 'modifierlivre.html', {'livre': livre})

def supprimer_livre(request):
    # Logique pour afficher la page de confirmation de suppression d'un livre
   
    return render(request, 'supprimer_livre.html', {'livre': livre})