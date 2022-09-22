from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data = MyWatchlist.objects.all()
    total_data = MyWatchlist.objects.count()
    cnt_watched = 0
    for i in data:
        if i.watched:
            cnt_watched += 1
            
    message = "Selamat, kamu sudah banyak menonton!"
    if cnt_watched < total_data:
        message = "Wah, kamu masih sedikit menonton!"
    context = {
        'data': data,
        'message': message
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )
