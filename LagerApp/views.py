from django.shortcuts import render,get_object_or_404
from .models import Article, Storage, Kennzahlen

# Create your views here.

def home(request):
    return render(request, 'LagerApp/home.html')

def article(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list,}
    return render(request, 'LagerApp/articles.html', context)

def lagerliste(request):
    lager_list = Storage.objects.all()
    context = {'lager_list': lager_list}
    return render(request, 'LagerApp/lagerliste.html', context)

def kennzahlen(request):
    return render(request, 'LagerApp/kennzahlen.html')

def lagerplatz(request, storage_id):
    lagerplatz = get_object_or_404(Storage, pk=storage_id)
    context = {'lager': lagerplatz}
    return render(request, 'LagerApp/lagerplatz.html', context)
