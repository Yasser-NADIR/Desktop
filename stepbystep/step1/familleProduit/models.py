from django.db import models

# Create your models here.

class FamilleProduit(models.Model):
	nomFamilleProduit = models.CharField(max_length=25)
	remarque = models.TextField()
	image = models.ImageField()

	def __str__(self):
		return self.nomFamilleProduit
	def get(self, arg):
		return self.__dict__.get(arg)

class Produit(models.Model):
	nomProduit = models.CharField(max_length=25)
	prixProduit = models.FloatField()
	qteProduit = models.IntegerField()
	familleProduit = models.ForeignKey('FamilleProduit', on_delete=models.CASCADE, related_name='produit')

	def __str__(self):
		return self.nomProduit