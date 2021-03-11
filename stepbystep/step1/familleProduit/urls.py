from django.urls import path
from . import views

app_name = 'familleProduit'

urlpatterns = [
	path('', views.familleProduit_ajout, name='familleProduit_ajout'),
	path('recherche/', views.familleProduit_recherche, name='familleProduit_recherche'),
	path('supprime/<int:id_fp>/', views.famillePoduit_supp, name='famillePoduit_supp'),
	path('modifie/<int:id_fp>/', views.famillePoduit_modifie, name='famillePoduit_modifie'),
	path('produit/', views.produit_ajout, name='produit_ajout'),
	path('produit/recherche/', views.produit_recherche, name='produit_recherche'),
	path('produit/supp/<int:id_produit>/', views.produit_supp, name='produit_supp'),
]
