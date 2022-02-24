from App import views
from django.urls import path

from App.views import AfficheP, AjoutProject

urlpatterns=[
    path('index/',views.index),
    path('index_p/<int:classe>/', views.index_para),
    path('Affiche/',views.Affiche),
    path('AfficheLV/',AfficheP.as_view(),name='AfficheLV'),
    path('Ajout/',views.Ajout,name='Ajout'),
    path('AjoutP/',AjoutProject.as_view(),name='AjoutP')

]