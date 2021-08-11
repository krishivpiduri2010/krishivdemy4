from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html', {'years': Year.objects.all(), 'months': Month.objects.all()
        , 'days': Date.objects.all()})


def page_view(request, pk):
    page = Page.objects.get(date=Date.objects.get(pk=pk))
    texts = Text.objects.filter(page=page)
    videos = Video.objects.filter(page=page)
    links = Link.objects.filter(page=page)
    items=[]
    items+=list(texts)
    items+=list(videos)
    items+=list(links)
    items.sort(key=lambda x:x.order)
    return render(request, 'page.html', {'years': Year.objects.all(), 'months': Month.objects.all()
        , 'days': Date.objects.all(), 'items':items})
