from django.db import models
from django.contrib.auth.models import User

class Pomysl(models.Model):
    tematyka = models.CharField(max_length=100)
    opis = models.TextField()
    planowane_korzysci = models.TextField(blank=True)
    planowane_koszty = models.TextField(blank=True)
    ocena_wazona = models.FloatField(null=True)

    status = models.ForeignKey(
        'StatusPomyslu',
        on_delete=models.CASCADE,
    )

    ustawienia_oceniania = models.ForeignKey(
        'UstawieniaOceniania',
        on_delete=models.CASCADE
    )

    uzytkownik = models.ForeignKey(
        'Uzytkownik',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.tematyka + ': ' + self.opis[:50] + '...'

class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=300)
    
    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class StatusPomyslu(models.Model):
    status = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.status

class UstawieniaOceniania(models.Model):
    ustawienia = models.CharField(max_length=200, primary_key=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.ustawienia

class Ocena(models.Model):
    data = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    ocena_liczbowa = models.IntegerField(null=True)
    opis = models.CharField(null=True, max_length=500)

    pomysl = models.ForeignKey(
        'Pomysl',
        on_delete=models.CASCADE,
    )

    uzytkownik = models.ForeignKey(
        'Uzytkownik',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.ocena_liczbowa

