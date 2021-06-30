from django.db import models

# Create your models here.
class problem(models.Model):
	name = models.CharField(max_length=500)
	url = models.URLField(max_length=400)
	tag = models.CharField(max_length=400)
	contest = models.CharField(max_length=10)
	search = models.CharField(max_length=500)