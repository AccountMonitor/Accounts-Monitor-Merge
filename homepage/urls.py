from django.urls import path
from . import views
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('homepage', views.homepage, name='homepage'),
    path('contact', views.contactMessage, name='contact'),
    path('newsletter', views.NewsLetter, name='newsletter')
]