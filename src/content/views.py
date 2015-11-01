from django.shortcuts import render
from .models import *

def home(request):
	sections = Section.objects.filter(is_active=True).order_by('title')
	context={
		'sections': sections,
	}
	return render_to_string(request, 'home.html', context)