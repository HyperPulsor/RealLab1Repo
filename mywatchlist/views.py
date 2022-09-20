from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import FilmWatch

# Create your views here.
def show_films(request):
    data_film = FilmWatch.objects.all()
    context = {
        'list_film' : data_film
    }
    return render(request, "mywatchlist.html", context)

def show_films_xml(request):
    data_film = FilmWatch.objects.all()
    return HttpResponse(serializers.serialize("xml", data_film), content_type="application/xml")

def show_films_json(request):
    data_film = FilmWatch.objects.all()
    return HttpResponse(serializers.serialize("json", data_film), content_type="application/json")