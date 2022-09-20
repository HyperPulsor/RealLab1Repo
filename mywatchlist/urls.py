from django.urls import path
from mywatchlist.views import show_films, show_films_xml, show_films_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_films, name='show_films'),
    path('xml/', show_films_xml, name='show_films_xml'),
    path('json/', show_films_json, name='show_films_json')
]