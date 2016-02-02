from django.db import models

# Create your models here

# Un destinatario es una persona a la que se debe entregar un paquete
class Destinatario(models.Model):
	direccion = models.CharField(max_length=100)
	ciudad = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.direccion

class Paquete(models.Model):
	contenido = models.CharField(max_length=100)
	valor = models.CharField(max_length=100)
	destinatario = models.ForeignKey(Destinatario)
	
	def __unicode__(self):
		return self.contenido
class Ruta(models.Model):
	nombre = models.CharField(max_length=100)
	paquetes = models.ManyToManyField(Paquete)
	
	def __unicode__(self):
		return self.nombre
