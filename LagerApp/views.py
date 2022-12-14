from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Article, Storage, Kennzahlen

# Create your views here.

def home(request):
    return render(request, 'LagerApp/home.html')

def article(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list,}
    return render(request, 'LagerApp/articles.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article,}
    return render(request, 'LagerApp/article_detail.html', context)

def lagerliste(request):
    lager_list = Storage.objects.all()
    context = {'lager_list': lager_list}
    return render(request, 'LagerApp/lagerliste.html', context)

def kennzahlen(request):
    kennzahlen = Kennzahlen.objects.all()
    umsatz = 0
    gewinn = 0
    abgänge = 0
    for kennzahl in kennzahlen:
        umsatz += kennzahl.umsatz
        gewinn += kennzahl.gewinn
        abgänge += kennzahl.abgänge
    context = {
        'umsatz': umsatz,
        'gewinn': gewinn,
        'abgänge': abgänge
    }
    return render(request, 'LagerApp/kennzahlen.html', context)

def lagerplatz(request, storage_id):
    lagerplatz = get_object_or_404(Storage, pk=storage_id)
    article_list = Article.objects.filter(storage=storage_id)
    context = {
        'lager': lagerplatz,
        'article_list': article_list
    }
    return render(request, 'LagerApp/lagerplatz.html', context)

def buchen(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        lagerplatz = get_object_or_404(Storage, pk=article.storage.id)
        kennzahl = get_object_or_404(Kennzahlen, pk=article.id)
        article_list = Article.objects.filter(storage=lagerplatz.id)
        try:
            amount = request.POST['menge']
            article.anzahl += int(amount)

            if (int(amount) > 0):
                kennzahl.gewinn += (int(amount) * article.ekpreis) * -1

            if (int(amount) < 0):
                kennzahl.umsatz += (int(amount) * article.vkpreis) * -1
                kennzahl.abgänge += int(amount) * -1
                kennzahl.gewinn += (int(amount) * article.vkpreis) * -1



        except ValueError as e:
            return render(request, 'LagerApp/lagerplatz.html', {
                'lager': lagerplatz,
                'article_list': article_list,
                'error_message': "OnlyNumbers",
            })
        else:
            article.save()
            kennzahl.save()
            return HttpResponseRedirect(reverse('LagerApp:lagerplatz', args=(lagerplatz.id,)))
