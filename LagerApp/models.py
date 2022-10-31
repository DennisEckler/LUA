from django.contrib import admin
from django.db import models

# Create your models here.

class Storage(models.Model):
    lagernummer = models.IntegerField()
    halle = models.IntegerField()
    Etage = models.IntegerField()
    Regal = models.IntegerField()
    
    def __str__(self):
        return str(self.lagernummer)

class Article(models.Model):
    artikelnummer = models.IntegerField()
    bezeichnung = models.CharField(max_length=255)
    anzahl = models.IntegerField()
    kategorie = models.CharField(max_length=150)
    lieferant = models.CharField(max_length=60)
    ekpreis = models.FloatField()
    vkpreis = models.FloatField()
    storage = models.ForeignKey(Storage, default=1, on_delete=models.CASCADE)

    @admin.display(
        ordering='artikelnummer',
        description='Artikelinfotest',
    )

    def setAmount(self, amount):
        self.anzahl += amount

    def __str__(self):
        return self.bezeichnung

class Kennzahlen(models.Model):
    maxbestand = models.IntegerField()
    minbestand = models.IntegerField()
    meldebestand = models.IntegerField()
    umsatz = models.FloatField()
    gewinn = models.FloatField()
    abgänge = models.IntegerField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'Kennzahlen zu {article}'
    
    class Meta:
        verbose_name_plural = 'Kennzahlen'