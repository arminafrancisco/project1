from django.views import generic
from content.models import *


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def home(request):
    	context = {
    		'sections': Section.objects.filter(is_active=True).order_by('title'),
    	}
    	return render_to_string(request, 'home.html', context)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
