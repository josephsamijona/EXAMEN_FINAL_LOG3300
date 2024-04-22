from django.shortcuts import render, redirect, get_object_or_404

from livres.models import Livres
from django.http import JsonResponse
from .forms import LivreForm


# on ajoute les methodes pour les urls afin que le render des pages html puisse se faire 
# Create your views here.
def home(request):
   livres = Livres.objects.all()
   return render(request, 'index.html', {'livres': livres})


def voir_livre(request, livre_id):
    livre = get_object_or_404(Livres, pk=livre_id)
    data = {
        'titre': livre.titre,
        'auteur': livre.auteur,
        'date_publication': livre.date_publication.strftime('%Y-%m-%d') if livre.date_publication else '',
        'genre': livre.genre
    }
    return JsonResponse(data)

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

def modifier_livre(request, livre_id):
    # Récupérer le livre à partir de son ID
    livre = get_object_or_404(Livres, pk=livre_id)
    
    if request.method == 'POST':
        # Si le formulaire est soumis avec des données, traiter les données
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            # Si le formulaire est valide, enregistrer les modifications
            form.save()
            return  redirect('home')  # Envoyer une réponse JSON pour indiquer le succès
    else:
        # Si c'est une requête GET, pré-remplir le formulaire avec les données du livre
        form = LivreForm(instance=livre)
    
    # Rendre le template avec le formulaire et les données du livre
    return render(request, 'modifierlivre.html', {'form': form, 'livre': livre})

def supprimer_livre(request, livre_id):
    # Récupérer le livre à supprimer
    livre = get_object_or_404(Livres, pk=livre_id)

    # Supprimer le livre
    livre.delete()

    # Redirection vers la page d'accueil ou une autre vue après la suppression
    return redirect('home') 