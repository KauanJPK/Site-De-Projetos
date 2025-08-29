from django.contrib import admin
from django.urls import path, include
from home.views import entrada
from sobre.views import sobre
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entrada, name='entrada'),
    path('sobre/', sobre),
]
