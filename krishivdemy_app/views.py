from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html', {'years': Year.objects.all(), 'months': Month.objects.all()
        , 'days': Date.objects.all()})


def page_view(request,pk):
    page=Page.objects.get(date=Date.objects.get(pk=pk))
    texts=Text.objects.filter(page=page)
    return render(request, 'page.html',{'years': Year.objects.all(), 'months': Month.objects.all()
        , 'days': Date.objects.all(),'page':page,'texts':texts})
