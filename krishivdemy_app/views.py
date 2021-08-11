from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html',{'years': Year.objects.all(), 'months': Month.objects.all()
        , 'days': Date.objects.all()})
