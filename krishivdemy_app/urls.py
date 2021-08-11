from .views import *
from django.urls import path

urlpatterns = [
    path('',home),
    path('page_view/<int:pk>',page_view,name='page_view')
]