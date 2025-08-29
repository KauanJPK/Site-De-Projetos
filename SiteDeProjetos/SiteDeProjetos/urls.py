from django.contrib import admin
from django.urls import path, include
from home.views import entrada
from sobre.views import sobre

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Aplicação rodando no Fly.io 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', entrada, name='entrada'),
    path('sobre/', sobre),
    path("", home),
]
