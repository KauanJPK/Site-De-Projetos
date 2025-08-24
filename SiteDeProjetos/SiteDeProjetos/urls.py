from django.contrib import admin
from django.urls import path, include
from home.views import entrada
from sobre.views import sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', entrada, name='entrada'),
    path('sobre/', sobre, name='sobre'),
]
