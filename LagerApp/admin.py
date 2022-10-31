from django.contrib import admin
from .models import Article, Storage, Kennzahlen

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields':['artikelnummer', 'bezeichnung', 'kategorie']}),
        ('Lagerinfo', {'fields':['storage', 'anzahl', 'lieferant']}),
        ('Preisinfo', {'fields':['ekpreis', 'vkpreis']}),
        )
    list_display = ('bezeichnung', 'artikelnummer', 'kategorie', 'anzahl')
    list_filter = ['storage']
    search_fields = ['kategorie']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Storage)
admin.site.register(Kennzahlen)
