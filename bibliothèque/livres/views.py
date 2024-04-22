from django.shortcuts import render



# on ajoute les methodes pour les urls afin que le render des pages html puisse se faire 
# Create your views here.
def home(request):
    # Logique pour récupérer la liste de tous les livres disponibles depuis la base de données
  
    return render(request, 'index.html' )

def livre(request ):
    # Logique pour récupérer les détails d'un livre spécifique en fonction de son ID
 
    return render(request, 'livre.html', {'livre': livre})

def ajout_livre(request):
    # Logique pour afficher le formulaire pour ajouter un nouveau livre
    return render(request, 'ajoutlivre.html')

def modifier_livre(request ):
    # Logique pour afficher le formulaire pour modifier les informations d'un livre existant
 
    return render(request, 'modifierlivre.html', {'livre': livre})

def supprimer_livre(request):
    # Logique pour afficher la page de confirmation de suppression d'un livre
   
    return render(request, 'supprimer_livre.html', {'livre': livre})