from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import About_pwares
from .models import Pwares_ratings
from .models import Pwares_services
from .models import Pwares_portfolio
from .models import Pwares_testimonials
from .models import Pwares_updates
from .models import Pwares_contacts

# Create your views here.
def index(request):
    aboutpwares = About_pwares.objects.all()
    pwaresrating = Pwares_ratings.objects.all()
    pwaresservices = Pwares_services.objects.all()
    pwaresportfolio = Pwares_portfolio.objects.all()
    pwarestestimonials = Pwares_testimonials.objects.all()
    pwaresupdates = Pwares_updates.objects.all()
    pwarescontacts = Pwares_contacts.objects.all()
    return render(request, 'index.html', {'aboutpwares':aboutpwares, 'pwaresrating':pwaresrating, 'pwaresservices':pwaresservices,
                  'pwaresportfolio':pwaresportfolio, 'pwarestestimonials':pwarestestimonials, 'pwaresupdates':pwaresupdates,
                  'pwarescontacts':pwarescontacts})
