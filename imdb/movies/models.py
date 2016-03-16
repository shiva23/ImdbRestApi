# from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
	name = models.CharField(max_length=50)	
	director = models.CharField(max_length=50)
	description = models.TextField()
	genre = models.CharField(max_length=150)
	rate = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	date = models.DateTimeField(auto_now=False, auto_now_add=True)

	owner = models.ForeignKey('auth.User')

	class Meta:
		ordering = ('date',)