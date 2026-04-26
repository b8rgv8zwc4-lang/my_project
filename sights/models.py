from django.db import models

CONTINENT_CHOICES = [
    ("Евразия", "Евразия"),
    ("Африка", "Африка"),
    ("Северная Америка", "Северная Америка"),
    ("Южная Америка", "Южная Америка"),
    ("Австралия", "Австралия"),
    ("Антарктида", "Антарктида"),
]


class BaseContinentSight(models.Model):
    sight_name = models.CharField("Название", max_length=32, default="unknown")
    sight_country = models.CharField("Место расположения", max_length=32, default="unknown")
    sight_information = models.TextField("Информация", max_length=1024, default="unknown")

    class Meta:
        abstract = True


class EurasiaSight(BaseContinentSight):
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES, default="unknown")
    euro_photo = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)


class SouthAmericaSight(BaseContinentSight):
    s_photo = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)


class NorthAmericaSight(BaseContinentSight):
    n_photo = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)


class AfricaSight(BaseContinentSight):
    sight_photo = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)


class AustraliaSight(BaseContinentSight):
    astrl_photo = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)


class MyMap(models.Model):
    routes = models.CharField("Названия маршрутов")


class TempUser(models.Model):
    username = models.CharField()
    password = models.CharField()


class Event(models.Model):
    events = models.CharField()


COUNTRY_PAGE_CHOICES = [
    ("Великобритания", "Великобритания"),
    ("Германия", "Германия"),
    ("Россия", "Россия"),
    ("Китай", "Китай"),
]


class MoreAboutCountry(models.Model):
    image = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)
    name = models.CharField("Название", max_length=32, default="unknown")
    country = models.CharField(
        "Месторасположение", max_length=32, default="unknown", choices=COUNTRY_PAGE_CHOICES
    )
    information = models.TextField("Информация", max_length=500, default="unknown")
    rating = models.IntegerField()


class Routes(models.Model):
    image = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)
    route_name = models.CharField("Название маршрута", max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=300, default="unknown")
    country = models.CharField("Место", max_length=32, default="unknown")


FOOD_TYPE_CHOICES = [
    ("cafe", "Кафе"),
    ("rest", "Ресторан"),
    ("fast", "Фастфуд"),
]


class FoodInCoiuntries(models.Model):
    types = models.CharField("Типы заведения", default="unknown", choices=FOOD_TYPE_CHOICES)
    name = models.CharField("Название заведения", default="unknown")
    place = models.CharField("Месторасположение", default="unknown")
    rating = models.IntegerField()
    image = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)
    information = models.TextField("Информация", max_length=500, default="unknown")


class Summary(models.Model):
    image = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)
    name = models.CharField("Название", max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=500, default="unknown")


class MainCard(models.Model):
    image = models.ImageField("Фото", upload_to="sights/", blank=True, null=True)
    country = models.CharField("Месторасположение", max_length=32, default="unknown")
    name = models.CharField("Название", max_length=32, default="unknown")
    information = models.TextField("Информация", max_length=300, default="unknown")
    rating = models.FloatField()


class UserReview(models.Model):
    author_name = models.CharField("Имя автора", max_length=80)
    sight_name = models.CharField("Название достопримечательности", max_length=120)
    rating = models.PositiveSmallIntegerField("Оценка", default=5)
    comment = models.TextField("Отзыв", max_length=500)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sight_name} ({self.rating}/5) - {self.author_name}"
