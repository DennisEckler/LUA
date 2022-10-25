from django.urls import path
from . import views

app_name ='LagerApp'
urlpatterns = [
    path('', views.index, name='index'),
]