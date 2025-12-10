from django.db import models

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
    
class FirstForm(models.Model):
    your_name = models.CharField("Ваше имя", max_length=32, default="Имя")
    your_surname = models.CharField("Ваша фамилия", max_length=32, default="Фамилия")
    visited_country = models.CharField("Где вы были", max_length=128, default="Посещённая страна")
    seen_sights = models.CharField("Что удивительного увидели", max_length=64, default="Что увидели")
    experience = models.TextField("Опыт", max_length=128, default="Опыт")
    

class BuyTourForm(models.Model):
    your_name = models.CharField("Ваше имя", max_length=32, default="Имя")
    your_surname = models.CharField("Ваша фамилия", max_length=32, default="Фамилия")
    your_patronimyc = models.CharField("Ваше отчество", max_length=32, default="Отчество")
    hotel_stars = models.CharField(
        max_length=10,
        choices=[
            ("2*","2*"),
            ("3*","3*"),
            ("4*","4*"),
            ("5*","5*"),],
        default="Количество звёзд",
        verbose_name="Количество звёзд")
    wished_country_for_visiting = models.CharField(
        max_length=32,
        choices=[
            ("Франция", "Франция"),
            ("Объединенные Арабские Эмираты", "Объединенные Арабские Эмираты"),
            ("Таиланд", "Таиланд"),
            ("Япония", "Япония"),
            ("Турция", "Турция"),
            ("Египет", "Египет"),
            ("Великобритания", "Великобритания"),
            ("Германия","Германия"),
            ("Марокко", "Марокко"),
            ("Китай", "Китай")],
        default="Куда поедите",
        verbose_name="Куда поедите"
    )
    adult_amount = models.IntegerField("Количество взрослых")
    children_amount = models.IntegerField("Количество детей")

class MyMap(models.Model):
    routes = models.CharField("Названия маршрутов")