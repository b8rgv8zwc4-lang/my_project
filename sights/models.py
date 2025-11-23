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
    your_name = models.CharField("Ваше имя", max_length=32, default="unknown")
    your_surname = models.CharField("Ваша фамилия", max_length=32, default="unknown")
    visited_country = models.CharField("Где вы были", max_length=128, default="unknown")
    seen_sights = models.CharField("Что удивительного увидели", max_length=64, default="unknown")
    experience = models.TextField("Опыт", max_length=128, default="unknown")