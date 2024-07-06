
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('shop/',shop,name='shop'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('dropdown/',dropdown,name='dropdown')

   
]
