from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
	path('', views.client_ajout, name="client_ajout"),
	path('recherche/', views.client_recherche, name="client_recherche"),
	path('supprime/<int:id_client>/', views.client_supp, name="client_supp"),
	path('modifie/<int:id_client>/', views.client_modifie, name="client_modifie"),
]