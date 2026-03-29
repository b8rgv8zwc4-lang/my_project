"""
URL configuration for world_sights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from sights.views import (main_page,
                          euro_page, 
                          south_page, 
                          north_page, 
                          africa_page, 
                          australia_page, 
                          create_event,
                          create_model_about_country,
                          create_routes,
                          create_food_in_countries,
                          create_quiz_page,
                          )
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings


def redirect_to_main_page(request):
    return redirect('sights/')


urlpatterns = [
    path('', redirect_to_main_page),
    path('admin/', admin.site.urls),
    path('sights/', main_page),
    path('sights/euro/', euro_page),
    path('sights/south_am/', south_page),
    path('sights/north_am/', north_page),
    path('sights/africa/', africa_page),
    path('sights/australia/', australia_page),
    path("sights/events/", create_event),
    path("sights/more/", create_model_about_country),
    path("sights/routes/", create_routes),
    path("sights/food/", create_food_in_countries),
    path("sights/quiz/", create_quiz_page),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)