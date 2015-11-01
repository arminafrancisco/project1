from django.db import models
import datetime
from django import forms
from django.forms import ModelForm


class Section(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField()
	display_initials = models.CharField(max_length=3)
	image = models.ImageField(upload_to ='categories/', blank=True, null=True)
	is_active = models.BooleanField('Active:')

	def __str__(self):
		return self.title