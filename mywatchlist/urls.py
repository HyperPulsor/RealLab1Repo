from django.urls import path
from mywatchlist.views import show_films, show_films_xml, show_films_json, show_not_watched

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_films, name='show_films'),
    path('xml/', show_films_xml, name='show_films_xml'),
    path('json/', show_films_json, name='show_films_json'),
    path('notwatched/', show_not_watched, name='show_not_watched')
]