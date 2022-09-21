from django.urls import path

from mywatchlist.views import show_html  
from mywatchlist.views import show_xml  
from mywatchlist.views import show_json 

# TODO: Implement Routings Here

app_name = 'mywatchlist'
urlpatterns = [
    path('html', show_html, name='html'),
    path('xml', show_xml, name='xml'),
    path('json', show_json, name='json'),
]