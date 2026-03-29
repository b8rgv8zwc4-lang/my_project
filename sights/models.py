from django.db import models
from django import forms
# Create your models here.

class EurasiaSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField( "Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")
    continent = models.CharField(
        max_length=50,
        choices=[
            ("Евразия", "Евразия"),
            ("Африка", "Африка"),
            ("Северная Америка", "Северная Америка"),
            ("Южная Америка", "Южная Америка"),
            ("Австралия", "Австралия"),
            ("Антарктида", "Антарктида"),
        ], default="unknown"
    )
    euro_photo = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    

    

class SouthAmericaSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField( "Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")
    s_photo = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)

class NorthAmericaSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField( "Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")
    n_photo = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    
class AfricaSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField( "Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")
    sight_photo = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    
class AustraliaSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField( "Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")
    astrl_photo = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    



class MyMap(models.Model):
    routes = models.CharField("Названия маршрутов")


class TempUser(models.Model):
    username = models.CharField()
    password = models.CharField()


class Event(models.Model):
    events = models.CharField()
    

class MoreAboutCountry(models.Model):
    image = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    name = models.CharField("Название", max_length=32, default="unknown",)
    country = models.CharField("Месторасположение", max_length=32, default="unknown",
                               choices=[
                                ("Великобритания", "Великобритания"),
                                ("Германия","Германия"),
                                ("Россия", "Россия"),
                                ("Китай", "Китай")
                            ])
    information = models.TextField("Информация", max_length=500, default="unknown")
    rating = models.IntegerField()

class Routes(models.Model):
    image = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    route_name = models.CharField("Название маршрута",max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=300, default="unknown")
    country = models.CharField("Место",max_length=32, default="unknown")


class FoodInCoiuntries(models.Model):
    types = models.CharField("Типы заведения", default="unknown",
        choices = 
        [('cafe', 'Кафе'),
          ('rest', 'Ресторан'),
            ('fast', 'Фастфуд')]
            )
    name = models.CharField("Название заведения", default="unknown")
    place = models.CharField("Месторасположение", default="unknown")
    rating = models.IntegerField()
    image = models.ImageField("Фото", upload_to='sights/',blank=True, null=True )
    information = models.TextField("Информация", max_length=500, default="unknown")


class Summary(models.Model):
    image = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    name = models.CharField("Название", max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=500, default="unknown")
    
class MainCard(models.Model):
    image = models.ImageField("Фото", upload_to='sights/', blank=True, null=True)
    country = models.CharField("Месторасположение", max_length=32, default="unknown")
    name = models.CharField("Название", max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=300, default="unknown")
    rating = models.FloatField()

