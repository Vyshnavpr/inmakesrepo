from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here
def demo(request):
     obj = Place.objects.all()
     obje = Team.objects.all()
     return render(request, "index.html", {'result': obj,'final': obje})


# Create your views here.
