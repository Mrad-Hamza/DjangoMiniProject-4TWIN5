from django import forms
from django.forms import Textarea
from django.views.generic import CreateView

from App.models import Projet


class AddProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields=('nom_projet','duree_projet','temps_alloue_createur','besoins','description','est_valide','createur')
        widgets={'besoins':Textarea(
            attrs={'cols':20,'rows':10}
        )}
