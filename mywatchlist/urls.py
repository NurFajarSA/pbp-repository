from django.urls import path

from mywatchlist.views import show_html, show_json, show_xml
# TODO: Implement Routings Here

app_name = 'mywatchlist'
urlpatterns = [
    path('html', show_html, name='html'),
    path('xml', show_xml, name='xml'),
    path('json', show_json, name='json'),
]