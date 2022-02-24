
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from App.forms import AddProjetForm
from App.models import Projet

# Create your views here.
def index(request):
    return HttpResponse('Bonjour les 4TWIN5')
def index_para(request,classe):
    return HttpResponse('Bonjour les 4TWIN5 %s'%classe)
def Affiche(request):
    projet=Projet.objects.all()
    resultat="-".join([p.nom_projet for p in projet])
    return render(request,'App/Affiche.html',{
        'p':projet
    })
class AfficheP(ListView):
    model = Projet
    template_name = 'App/Affiche.html'
    context_object_name = 'p'
    #list_display=('nom_projet','besoins')

# bech nasn3ou requete w form
def Ajout(request):
    if request.method=="GET":
        form=AddProjetForm()
        return render(request,'App/Ajout.html',{'f':form})
    if request.method=="POST":
        form=AddProjetForm(request.POST)
        if form.is_valid():
            new_projet=form.save(commit=False)
            #récupere les instances non sauvegardés
            new_projet.save()
            return HttpResponseRedirect(reverse('AfficheLV'))
        else:
            return render(request,'App/Ajout.html',{'f':form,'msg_erreur':"Erreur lors de l'ajout"})


# juste na3tiw fields w yasna3 automatiquement form w requete => classe générique
class AjoutProject(CreateView):
    model=Projet
    fields = ('nom_projet', 'duree_projet', 'temps_alloue_createur', 'besoins', 'description', 'est_valide', 'createur')
    success_url = reverse_lazy('AfficheLV')