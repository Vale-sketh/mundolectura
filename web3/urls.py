from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mislibros/', views.mislibros, name='mislibros'),
    path('generos/', views.generos, name='generos'),
    path('recomendados/', views.recomendados, name='recomendados'),
]