from django.contrib import admin
from .models import Article, Storage, Kennzahlen

# Register your models here.

admin.site.register(Article)
admin.site.register(Storage)
admin.site.register(Kennzahlen)
