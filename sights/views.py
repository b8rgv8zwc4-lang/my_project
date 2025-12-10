from re import S
from django.conf import settings
from pathlib import Path
from django.shortcuts import render
from .models import (EurasiaSight, 
                     SouthAmericaSight, 
                     NorthAmericaSight, 
                     AfricaSight, 
                     AustraliaSight, 
                     FirstForm,
                     BuyTourForm,
                     MyMap)

from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def main_page(request):
    # Load large intro text from a plain text file
    text_file_path: Path = settings.BASE_DIR / 'sights' / 'static' / 'sights' / 'text' / 'main_page_intro.txt'
    try:
        main_intro = text_file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        main_intro = ''
    return render(request, 'sights/main_page.html', {"main_intro": main_intro})


def euro_page(request): 
    sight = EurasiaSight.objects.all()
    return render(request, 'sights/euro.html', {"sight": sight})    

def south_page(request):
    s_sight = SouthAmericaSight.objects.all()
    return render(request, 'sights/south_am.html', {"s_sight": s_sight})

def north_page(request):
    n_sight = NorthAmericaSight.objects.all()
    return render(request, 'sights/north_am.html', {"n_sight": n_sight})

def africa_page(request):
    a_sight = AfricaSight.objects.all()
    return render(request, 'sights/africa.html', {"a_sight": a_sight})

def australia_page(request):
    astrl_sight = AustraliaSight.objects.all()
    return render(request, 'sights/australia.html', {"astrl_sight":astrl_sight})


class CreateForm(CreateView):
    model = FirstForm
    fields = "__all__"
    template_name = "sights/form.html"
    success_url = reverse_lazy("info")

def info_page(request):
    info = FirstForm.objects.all()
    return render(request, 'sights/information_about_people.html', {"info": info})

class CreateFormForBuyingTour(CreateView):
    model = BuyTourForm
    fields = "__all__"
    template_name = "sights/buy_tour.html"
    success_url = reverse_lazy("information")

def info_buy_tour_page(request):
    information = BuyTourForm.objects.all()
    return render(request, 'sights/info_buy_tour.html', {"info": information})
   
def create_map(request):
    map = MyMap.objects.all()
    return render(request, 'sights/routes.html', {"map": map})
