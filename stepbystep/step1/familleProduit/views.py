from django.shortcuts import render, redirect
from .models import FamilleProduit, Produit
from .forms import FamilleProduitForm, SearchForm, ProduitForm

# Create your views here.


def familleProduit_ajout(request):
	msg = None
	if request.method == 'POST':
		fp = FamilleProduitForm(request.POST, request.FILES)
		if fp.is_valid():
			cd = fp.cleaned_data
			#print(cd)
			FamilleProduit.objects.create(**cd)
			msg = "famille produit ajouté"

	form = FamilleProduitForm()
	return render(request, 'familleProduit/ajout.html', {'form': form, 'msg' : msg})

	
def familleProduit_recherche(request):
	if request.method == 'POST':
		fp_all = FamilleProduit.objects.filter(nomFamilleProduit__contains=request.POST.get("nom"))
	else:
		fp_all = FamilleProduit.objects.all()
	form = SearchForm()
	return render(request, 'familleProduit/recherche.html', {'form': form, 'fp_all': fp_all})

def famillePoduit_supp(request, id_fp):
	fp = FamilleProduit.objects.get(id=id_fp)
	if request.method == "POST":
		fp.delete()
		return redirect('familleProduit:familleProduit_recherche')
	
	return render(request, 'familleProduit/supp.html', {'fp': fp})

def famillePoduit_modifie(request, id_fp):
	fp = FamilleProduit.objects.get(id=id_fp)
	if request.method == "POST":
		fp.nomFamilleProduit = request.POST.get('nomFamilleProduit')
		fp.remarque = request.POST.get('remarque')
		fp.save()
		return redirect('familleProduit:familleProduit_recherche')
	form = FamilleProduitForm(fp)
	return render(request, 'familleProduit/modifier.html', {'form': form})

def produit_ajout(request):
	form = ProduitForm()
	if request.method == 'POST':
		f = ProduitForm(request.POST)
		if f.is_valid():
			cd = f.cleaned_data
			Produit.objects.create(**cd)
	return render(request, 'produit/ajout.html', {'form': form})

def produit_recherche(request):
	form = SearchForm()
	produit_all = Produit.objects.all()
	return render(request, 'produit/recherche.html', {'form': form, 'p_all': produit_all})

def produit_supp(request, id_produit):
	produit = Produit.objects.get(id=id_produit)
	if request.method == 'POST':
		produit.delete()
		return redirect('familleProduit:produit_recherche')
	return render(request, 'produit/supp.html', {'produit': produit})