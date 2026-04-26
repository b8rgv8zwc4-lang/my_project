from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import (
    AfricaSight,
    AustraliaSight,
    EurasiaSight,
    Event,
    FoodInCoiuntries,
    MainCard,
    MoreAboutCountry,
    NorthAmericaSight,
    Routes,
    SouthAmericaSight,
    Summary,
    UserReview,
)


def _continent_page(request, model, template, sights_key):
    qs = model.objects.all()
    countries = (
        model.objects.values_list("sight_country", flat=True).distinct().order_by("sight_country")
    )
    selected_country = request.GET.get("country", "")
    if selected_country:
        qs = qs.filter(sight_country=selected_country)
    return render(
        request,
        template,
        {
            sights_key: qs,
            "countries": countries,
            "selected_country": selected_country,
        },
    )


def _object_list(request, model, template, context_key):
    return render(request, template, {context_key: model.objects.all()})


def main_page(request):
    return render(request, "sights/main_page.html", {"card": MainCard.objects.all()})


def euro_page(request):
    return _continent_page(request, EurasiaSight, "sights/euro.html", "sight")


def south_page(request):
    return _continent_page(request, SouthAmericaSight, "sights/south_am.html", "s_sight")


def north_page(request):
    return _continent_page(request, NorthAmericaSight, "sights/north_am.html", "n_sight")


def africa_page(request):
    return _continent_page(request, AfricaSight, "sights/africa.html", "a_sight")


def australia_page(request):
    return _continent_page(request, AustraliaSight, "sights/australia.html", "astrl_sight")


def create_event(request):
    return _object_list(request, Event, "sights/events.html", "event")


def create_model_about_country(request):
    return _object_list(request, MoreAboutCountry, "more/more_china.html", "more_about_country")


def create_routes(request):
    return _object_list(request, Routes, "sights/routes_countries.html", "routes")


def create_food_in_countries(request):
    return _object_list(request, FoodInCoiuntries, "sights/food.html", "food")


def create_summary(request):
    return _object_list(request, Summary, "sights/summary.html", "summary")


def create_quiz_page(request):
    return render(request, "sights/quiz.html")


def login_view(request):
    """Authenticate and redirect to main page on success."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/sights/")
        else:
            messages.error(request, "Неверный логин или пароль")

    return render(request, "sights/login_page.html")


def reviews_page(request):
    if request.method == "POST":
        author_name = request.POST.get("author_name", "").strip()
        sight_name = request.POST.get("sight_name", "").strip()
        comment = request.POST.get("comment", "").strip()
        rating_raw = request.POST.get("rating", "5").strip()

        if not (author_name and sight_name and comment):
            messages.error(request, "Заполните все поля формы.")
            return redirect("/sights/reviews/")

        try:
            rating = int(rating_raw)
        except ValueError:
            rating = 5

        rating = max(1, min(5, rating))
        UserReview.objects.create(
            author_name=author_name,
            sight_name=sight_name,
            comment=comment,
            rating=rating,
        )
        messages.success(request, "Спасибо! Ваш отзыв добавлен.")
        return redirect("/sights/reviews/")

    reviews = UserReview.objects.all()
    return render(request, "sights/reviews.html", {"reviews": reviews})
