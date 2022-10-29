from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    context = {'article_list': article_list,}
    return render(request, 'LagerApp/index.html', context)