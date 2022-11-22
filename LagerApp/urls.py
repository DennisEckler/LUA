from django.urls import path
from . import views

app_name ='LagerApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('article/', views.article, name='article'),
    path('article/<int:article_id>', views.detail, name='detail'),
    path('lagerliste/', views.lagerliste, name='lagerliste'),
    path('kennzahlen/', views.kennzahlen, name='kennzahlen'),
    path('lagerliste/<int:storage_id>/', views.lagerplatz, name='lagerplatz'),
    path('article/<int:article_id>/buchen', views.buchen, name='buchen'),
]
