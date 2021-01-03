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
    sso = models.CharField(max_length=9)
    
    def __str__(self):
        return self.imie + ' ' + self.nazwisko + ' ' + self.sso


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
        return "Ocena id: {}, liczbowa: {}, opis: {}, uzytkownik: {}".format(
            self.pk, self.ocena_liczbowa, self.opis, self.uzytkownik)

class Decyzja(models.Model):
    data=models.DateTimeField('%Y-%m-%d %H:%M:%S')
    uzasadnienie=models.CharField(max_length=1000)
    pomysl = models.ForeignKey(
        'Pomysl',
        on_delete=models.CASCADE,
    )
    uzytkownik = models.ForeignKey(
        'Uzytkownik',
        on_delete=models.CASCADE,
    )
    werdykt=models.ForeignKey(
        'RodzajDecyzji',
        on_delete=models.CASCADE,
    )


class RodzajDecyzji(models.Model):
    rodzaj_decyzji = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.rodzaj_decyzji

class CzlonekKomisji(models.Model):
    uzytkownik = models.OneToOneField(
        'Uzytkownik',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.uzytkownik

class Administrator(models.Model):
    uzytkownik = models.OneToOneField(
        'Uzytkownik',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.uzytkownik

class ZwyklyUzytkownik(models.Model):
    uzytkownik = models.OneToOneField(
        'Uzytkownik',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.uzytkownik
