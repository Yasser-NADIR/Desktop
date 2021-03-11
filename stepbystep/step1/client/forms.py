from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ('nom','tele','addresse')

class ClientSearchForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ('nom',)
	

