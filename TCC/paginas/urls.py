from django.urls import path
from .views import PaginaInicial, SobreView

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index.html'),
    path('sobre/', SobreView.as_view(), name='sobre.html'),
]