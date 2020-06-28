from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>This is the Music home page</H1>")
def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id :" + str(album_id)+"</h2>")