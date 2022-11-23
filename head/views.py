from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    categorias = Categorias.objects.filter()
    return render(request,'demo/home.html',{"categorias": categorias})