from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Album
from django.template import loader
def index(request):

    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context, request))
def detail(request, album_id):
    template = loader.get_template('music/albumid.html')
    context = {
        'all_albums': album_id,
    }
    return HttpResponse(template.render(context, request))