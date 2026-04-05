from django.shortcuts import redirect, render
from .models import (EurasiaSight, 
                     SouthAmericaSight, 
                     NorthAmericaSight, 
                     AfricaSight, 
                     AustraliaSight, 
                     Event,
                     MoreAboutCountry,
                     Routes,
                    FoodInCoiuntries,
                    Summary,
                    MainCard,
                    )



from django.views.generic import CreateView

def main_page(request):
    card = MainCard.objects.all()
    return render(request, 'sights/main_page.html', {"card": card})


def euro_page(request): 
    sight = EurasiaSight.objects.all()
    
    #  Здесь получаем уникальные страны для фильтра
    countries = EurasiaSight.objects.values_list('sight_country', flat=True).distinct().order_by('sight_country')
    
    # Фильтрация по стране из GET параметра
    selected_country = request.GET.get('country', '')
    if selected_country:
        sight = sight.filter(sight_country=selected_country)
    
    return render(request, 'sights/euro.html', {
        "sight": sight,
        "countries": countries,
        "selected_country": selected_country
    })

def south_page(request):
    s_sight = SouthAmericaSight.objects.all()
    countries = SouthAmericaSight.objects.values_list('sight_country', flat=True).distinct().order_by('sight_country')
    
    # Фильтрация по стране из GET параметра
    selected_country = request.GET.get('country', '')
    if selected_country:
        s_sight = s_sight.filter(sight_country=selected_country)
    
    return render(request, 'sights/south_am.html', {
        "s_sight": s_sight,
        "countries": countries,
        "selected_country": selected_country
    })
   


def north_page(request):
    n_sight = NorthAmericaSight.objects.all()
    countries = NorthAmericaSight.objects.values_list('sight_country', flat=True).distinct().order_by('sight_country')
    
    # Фильтрация по стране из GET параметра
    selected_country = request.GET.get('country', '')
    if selected_country:
        n_sight = n_sight.filter(sight_country=selected_country)
    
    return render(request, 'sights/north_am.html', {
        "n_sight": n_sight,
        "countries": countries,
        "selected_country": selected_country
    })
   


def africa_page(request):
    a_sight = AfricaSight.objects.all()
    
    # Получаем уникальные страны для фильтра
    countries = AfricaSight.objects.values_list('sight_country', flat=True).distinct().order_by('sight_country')
    
    # Фильтрация по стране из GET параметра
    selected_country = request.GET.get('country', '')
    if selected_country:
        a_sight = a_sight.filter(sight_country=selected_country)
    
    return render(request, 'sights/africa.html', {
        "a_sight": a_sight,
        "countries": countries,
        "selected_country": selected_country
    })

def australia_page(request):
    astrl_sight = AustraliaSight.objects.all()
    countries = AustraliaSight.objects.values_list('sight_country', flat=True).distinct().order_by('sight_country')
    
    # Фильтрация по стране из GET параметра
    selected_country = request.GET.get('country', '')
    if selected_country:
        astrl_sight = astrl_sight.filter(sight_country=selected_country)
    
    return render(request, 'sights/australia.html', {
        "astrl_sight": astrl_sight,
        "countries": countries,
        "selected_country": selected_country
    })





def create_event(request):
    event = Event.objects.all()
    return render(request, 'sights/events.html', {"event": event})


def create_model_about_country(request):
    more_about_country = MoreAboutCountry.objects.all()
    return render(request, "more/more_china.html", {"more_about_country": more_about_country})


def create_routes(request):
    routes = Routes.objects.all()
    return render(request, "sights/routes_countries.html", {"routes": routes})


def create_food_in_countries(request):
    food = FoodInCoiuntries.objects.all()
    return render(request, "sights/food.html", {"food": food})


def create_summary(request):
    summary = Summary.objects.all()
    return render(request, "sights/summary.html", {"summary": summary})


def create_quiz_page(request):
    return render(request, "sights/quiz.html")


