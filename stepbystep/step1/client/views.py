from django.shortcuts import render, redirect
from .forms import ClientForm, ClientSearchForm
from .models import Client
from django.urls import reverse

# Create your views here.

def client_ajout(request):
	done = False
	if request.method == 'POST':
		client_form = ClientForm(request.POST)
		if client_form.is_valid():
			cd = client_form.cleaned_data
			Client.objects.create(**cd)
			done = True
			client_form = ClientForm()
	else:
		client_form = ClientForm()
	to_recherche = request.build_absolute_uri(reverse("client:client_recherche"))
	return render(request, 'client/ajout.html', {'form':client_form, 'done': done, "recherche": to_recherche})

def client_recherche(request):
	msg = None
	if request.method == 'POST':
		clients = Client.objects.filter(nom=request.POST["nom"])
		if len(clients) == 0:
			msg = "pas de resultat"
	else:
		clients = Client.objects.all()
		if len(clients) == 0:
			msg = "aucun client n'est enregisté"
	form = ClientSearchForm()
	liste = []
	for client in clients:
		liste.append(
			(client, 
				request.build_absolute_uri(reverse("client:client_supp", args=[client.id])),
				request.build_absolute_uri(reverse("client:client_modifie", args=[client.id]))),
			)
	return render(request, 'client/recherche.html', 
		{'form':form, "msg": msg, 'clients': clients, 
		'len': len(clients), "liste": liste})


def client_supp(request, id_client=None):
	client = Client.objects.filter(id=id_client).first()
	if request.method == "POST":
		client.delete()
		return redirect("client:client_recherche")
	return render(request, 'client/supprime.html', {"client": client})

def client_modifie(request, id_client=None):
	client = Client.objects.get(id=id_client)
	client_form = ClientForm(client)
	if request.method == "POST":
		client_form = ClientForm(request.POST)
		if client_form.is_valid():
			cd = client_form.cleaned_data
			client.nom = cd['nom']
			client.tele = cd['tele']
			client.addresse = cd['addresse']
			client.save()
			return redirect("client:client_recherche")

	return render(request, 'client/modife.html', {"form": client_form, "client": client})

