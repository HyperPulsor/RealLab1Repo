from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import FilmWatch

# Create your views here.
def show_films(request):
    data_film = FilmWatch.objects.all()

    sum_watched = 0
    sum_not_watched = 0

    for films in data_film :
        if (films.watched):
            sum_watched += 1
        else:
            sum_not_watched += 1

    if (sum_watched >= sum_not_watched):
        context = {
        'list_film' : data_film,
        'bonus' : "Selamat, kamu sudah banyak menonton!",
        'sum_watched' : sum_watched,
        'sum_not_watched' : sum_not_watched
        }
    else :
        context = {
        'list_film' : data_film,
        'bonus' : "Wah, kamu masih sedikit menonton!",
        'sum_watched' : sum_watched,
        'sum_not_watched' : sum_not_watched
        }
    
    return render(request, "mywatchlist.html", context)

def show_films_xml(request):
    data_film = FilmWatch.objects.all()
    return HttpResponse(serializers.serialize("xml", data_film), content_type="application/xml")

def show_films_json(request):
    data_film = FilmWatch.objects.all()
    return HttpResponse(serializers.serialize("json", data_film), content_type="application/json")