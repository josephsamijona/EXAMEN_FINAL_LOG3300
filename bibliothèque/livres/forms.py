from django import forms
from .models import Livres


 
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livres
        fields = ['titre', 'auteur', 'date_publication', 'genre']
        widgets = {
            'date_publication': forms.DateInput(attrs={'type': 'date'})
        }
