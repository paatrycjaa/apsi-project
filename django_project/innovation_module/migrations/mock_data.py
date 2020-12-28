import random 

from django.contrib.auth.models import User
from django.db import migrations
from django.db import migrations

app = 'innovation_module'

def make_migrations(apps, schema_editor):
    create_status_pomyslu(apps)
    create_ustawienia_oceniania(apps)
    create_uzytkownik(apps)
    create_pomysl(apps)
    create_ocena(apps)
    add_role_to_uzytkownik(apps)


def create_status_pomyslu(apps):
    StatusPomyslu = apps.get_model(app, 'StatusPomyslu')

    statuses = ['Oczekujacy', 'Edycja', 'Zablokowany', 'Odlozony', 'Zaakceptowany', 'Odrzucony']

    for status in statuses:
        m = StatusPomyslu(status=status)
        m.save()


def create_ustawienia_oceniania(apps):
    UstawieniaOceniania = apps.get_model(app, 'UstawieniaOceniania')

    settings = [
        ('brak', 'Brak możliwości oceniania'),
        ('num_text', 'Ocena liczbowa i słowna'),
        ('num_only', 'Tylko ocena liczbowa'),
        ('text_only', 'Tylko ocena słowna'),
    ]

    for s in settings:
        m = UstawieniaOceniania(ustawienia=s[0], opis=s[1])
        m.save()


def create_uzytkownik(apps):
    Uzytkownik = apps.get_model(app, 'Uzytkownik')

    users = [
        # name, surname, sso, username, email, password
        ('Janusz', 'Chmielewski', '100', 'sso100', '', 'useruser'),
        ('Ludwik', 'Mróz', '101', 'sso101', '', 'useruser'),
        ('Fabian', 'Szczepański', '102', 'sso102', '', 'useruser'),
        ('Albert', 'Malinowski', '103', 'sso103', '', 'useruser'),
        ('Olaf', 'Rutkowski', '104', 'sso104', '', 'useruser'),
        ('Natasza', 'Sikorska', '105', 'sso105', '', 'useruser'),
        ('Ilona', 'Pietrzak', '106', 'sso106', '', 'useruser'),
        ('Nikola', 'Sikora', '107', 'sso107', '', 'useruser'),
        ('Wioletta', 'Adamska', '108', 'sso108', '', 'useruser'),
        ('Izabela', 'Sikorska', '109', 'sso109', '', 'useruser')
    ]

    for _user in users:
        u = User.objects.create_user(_user[3], _user[4], _user[5])
        u.first_name = _user[0]
        u.last_name = _user[1]
        u.save()
        
        u = User.objects.get(username=_user[3])
        m = Uzytkownik(imie=_user[0], nazwisko=_user[1], sso=_user[2])
        m.save()

def add_role_to_uzytkownik(apps):
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    CzlonekKomisji = apps.get_model(app, 'CzlonekKomisji')
    Administrator = apps.get_model(app, 'Administrator')
    ZwyklyUzytkownik = apps.get_model(app, 'ZwyklyUzytkownik')

    users = Uzytkownik.objects.all()

    a = Administrator(uzytkownik=users[0])
    a.save()

    for i in range(1, 3):
        ck = CzlonekKomisji(uzytkownik=users[i])
        ck.save()

    for i in range(3, len(users)):
        zu = ZwyklyUzytkownik(uzytkownik=users[i])
        zu.save()

def create_pomysl(apps):

    Pomysl = apps.get_model(app, 'Pomysl')
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    StatusPomyslu = apps.get_model(app, 'StatusPomyslu')
    UstawieniaOceniania = apps.get_model(app, 'UstawieniaOceniania')

    ideas = [
        ('Nowe komputery', 'Kupmy wiecej komputerów', 'Będą nowe komputery', 'Koszty komputerów', '5'),
        ('Nowe drukarki', 'Kupmy wiecej drukarek', 'Będą nowe drukarki', 'Koszty drukarek', '8'),
        ('Nowe X', 'Kupmy wiecej X', 'Będą nowe X', 'Koszty X', '7'),
        ('Nowe Y', 'Kupmy wiecej Y', 'Będą nowe Y', 'Koszty Y', '6'),
        ('Nowe Z', 'Kupmy wiecej Z', 'Będą nowe Z', 'Koszty Z', '2'),
        ('Lepsze komputery', 'Kupmy lepsze komputery', 'Będą lepsze komputery', 'Koszty lepszych komputerów', '10'),
        ('Lepsze drukarki', 'Kupmy lepsze drukarki', 'Będą lepsze drukarki', 'Koszty lepszych drukarek', '8'),
        ('Lepsze X', 'Kupmy lepsze X', 'Będą lepsze X', 'Koszty lepszych X', '7'),
        ('Lepsze Y', 'Kupmy lepsze Y', 'Będą lepsze Y', 'Koszty lepszych Y', '6'),
        ('Lepsze Z', 'Kupmy lepsze Z', 'Będą lepsze Z', 'Koszty lepszych Z', '9')
    ]

    users = Uzytkownik.objects.all()
    # statuses = StatusPomyslu.objects.all()
    settings = UstawieniaOceniania.objects.all()

    for i in ideas:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')
        setting = random.choice(settings)

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status=status, ustawienia_oceniania=setting, uzytkownik=user)
        m.save()


def create_ocena(apps):
    Ocena = apps.get_model(app, 'Ocena')
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    Pomysl = apps.get_model(app, 'Pomysl')

    opinions = [
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
        ('2020-12-10 12:00:00', 6, 'Bardzo dobry pomysl'),
    ]

    users = Uzytkownik.objects.all()
    ideas = Pomysl.objects.all()

    for opinion in opinions:
        idea = random.choice(ideas)
        user = random.choice([u for u in users if u is not idea.uzytkownik])

        m = Ocena(data=opinion[0], ocena_liczbowa=opinion[1], opis=opinion[2], pomysl=idea, uzytkownik=user)
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        (app, '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_migrations)
    ]
