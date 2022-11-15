from django.urls import path
from . import views

app_name ='LagerApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('article/', views.article, name='article'),
    path('lagerliste/', views.lagerliste, name='lagerliste'),
    path('kennzahlen/', views.kennzahlen, name='kennzahlen'),
    path('lagerliste/<int:storage_id>/', views.lagerplatz, name='lagerplatz'),
]
