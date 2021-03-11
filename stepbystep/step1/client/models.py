from django.db import models

# Create your models here.


class Client(models.Model):
	nom = models.CharField(max_length=25)
	tele = models.CharField(max_length=250)
	addresse = models.CharField(max_length=250)

	def __str__(self):
		return self.nom
	def get(self, arg):
		return self.__dict__[arg]