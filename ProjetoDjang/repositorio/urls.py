from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('relatorios.urls')),
    path('admin/', admin.site.urls),
]
