from django.urls import path
from django.urls import reverse
from . import views
from django.http import HttpResponse
urlpatterns = [
    path('',views.home,name='home')
]
