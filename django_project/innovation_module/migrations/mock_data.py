import random 

from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.db import migrations
from django.db import migrations

app = 'innovation_module'

def make_migrations(apps, schema_editor):
    create_status_pomyslu(apps)
    create_ustawienia_oceniania(apps)
    create_uzytkownik(apps)
    create_pomysl(apps)
    create_ocena(apps)
    create_rodzaj_decyzji(apps)
    create_watek(apps)
    create_post(apps)
    add_role_to_uzytkownik(apps)


def create_status_pomyslu(apps):
    StatusPomyslu = apps.get_model(app, 'StatusPomyslu')

    statuses = ['Oczekujacy', 'Edycja', 'Zablokowany', 'Odlozony', 'Zaakceptowany', 'Odrzucony']

    for status in statuses:
        m = StatusPomyslu(status=status)
        m.save()

def create_rodzaj_decyzji(apps):
    RodzajDecyzji = apps.get_model(app, 'RodzajDecyzji')

    rodzaje_decyzji = ['Zaakceptowany', 'Odrzucony', 'Prosba o uzupelnienie', 'Odlozony']

    for rodzaj_decyzji in rodzaje_decyzji:
        m = RodzajDecyzji(rodzaj_decyzji=rodzaj_decyzji)
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
    User = apps.get_model(settings.AUTH_USER_MODEL)

    users = [
        # name, surname, sso, username, email, password, is superuser, is staff
        ('Janusz', 'Chmielewski', '100', 'sso100', '', 'useruser', True, True),
        ('Ludwik', 'Mróz', '101', 'sso101', '', 'useruser', False, False),
        ('Fabian', 'Szczepański', '102', 'sso102', '', 'useruser', False, False),
        ('Albert', 'Malinowski', '103', 'sso103', '', 'useruser', False, False),
        ('Olaf', 'Rutkowski', '104', 'sso104', '', 'useruser', False, False),
        ('Natasza', 'Sikorska', '105', 'sso105', '', 'useruser', False, False),
        ('Ilona', 'Pietrzak', '106', 'sso106', '', 'useruser', False, False),
        ('Nikola', 'Sikora', '107', 'sso107', '', 'useruser', False, False),
        ('Wioletta', 'Adamska', '108', 'sso108', '', 'useruser', False, False),
        ('Izabela', 'Sikorska', '109', 'sso109', '', 'useruser', False, False)
    ]

    for user in users:
        u, _ = User.objects.get_or_create(username=user[3], email=user[4], first_name=user[0], last_name=user[1], is_superuser=user[6], is_staff=user[7])
        u.password = make_password(user[5])
        u.save()

        Uzytkownik.objects.create(
            user=u, 
            imie=user[0], 
            nazwisko=user[1], 
            sso=user[2]
        )

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

    for i in ideas[:4]:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')
        setting = random.choice(settings)

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status=status, ustawienia_oceniania=setting, uzytkownik=user)
        m.save()

    for idx, i in enumerate(ideas[4:]):
        statuses = ['Oczekujacy', 'Edycja', 'Zablokowany', 'Odlozony', 'Zaakceptowany', 'Odrzucony']
        user = Uzytkownik.objects.get(sso='109')
        status = StatusPomyslu.objects.get(status=statuses[idx])
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

def create_watek(apps):
    Watek = apps.get_model(app, 'Watek')

    threads = [
        ('Temat 1', '2020-12-27 12:00:00', '2020-12-29 12:00:00'),
        ('Temat 2', '2020-12-26 12:00:00', '2020-12-28 12:00:00'),
        ('Temat 3', '2020-12-25 12:00:00', '2020-12-27 12:00:00'),
    ]

    for thread in threads:
        m = Watek(temat=thread[0], data_dodania =thread[1], data_ostatniego_posta =thread[2])
        m.save()
    
def create_post(apps):
    Post = apps.get_model(app, 'Post')
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    Watek = apps.get_model(app, 'Watek')

    posts = [
        ('Tytul 1', 'Tresc posta', '2020-12-29 17:00:00'),
        ('Tytul 2', 'Tresc posta', '2020-12-28 06:00:00'),
        ('Tytul 3', 'Tresc posta', '2020-12-29 13:00:00'),
        ('Tytul 4', 'Tresc posta', '2020-12-28 12:00:00'),
        ('Tytul 5', 'Tresc posta', '2020-12-29 15:00:00'),
        ('Tytul 6', 'Tresc posta', '2020-12-28 20:00:00'),
        ('Tytul 7', 'Tresc posta', '2020-12-29 12:00:00'),
    ]

    users = Uzytkownik.objects.all()
    threads = Watek.objects.all()

    for post in posts:
        user = random.choice(users)
        thread = random.choice(threads)

        m = Post(tytul=post[0], tresc=post[1], watek = thread, uzytkownik= user,data_dodania=post[2])
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        (app, '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_migrations)
    ]
