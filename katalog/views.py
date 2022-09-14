from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    catalog_data = CatalogItem.objects.all()
    context = {
        'catalog_data': catalog_data,
        'name': 'Nur Fajar',
        'id': '2106751114'
    }
    return render(request, 'katalog.html', context)
