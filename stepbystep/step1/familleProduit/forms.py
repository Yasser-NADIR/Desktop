from django import forms
from .models import FamilleProduit, Produit

class FamilleProduitForm(forms.ModelForm):

	def __init__(self, *arg, **kwarg):
		super(FamilleProduitForm, self).__init__(*arg, **kwarg)
		self.fields['remarque'].required = False

	class Meta:
		model = FamilleProduit
		fields = '__all__'

class SearchForm(forms.Form):
	nom = forms.CharField(max_length=25, required=True)

class ProduitForm(forms.ModelForm):
	class Meta:
		model = Produit
		fields = '__all__'
