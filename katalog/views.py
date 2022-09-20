from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    #
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Rakan Fasya Athhar Rayyan',
    'npm' : '2106750950'
}
    return render(request, "katalog.html", context)
