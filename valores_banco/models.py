from django.db import models

# Create your models here.

class valorModel(models.Model):
	valor_banco_brasil = models.BigIntegerField()
	valor_banco_bradesco = models.BigIntegerField()
	
class newsModel(models.Model):
	title = models.CharField(max_length = 1000)
	text = models.CharField(max_length = 1000)
	date = models.CharField(max_length = 30)