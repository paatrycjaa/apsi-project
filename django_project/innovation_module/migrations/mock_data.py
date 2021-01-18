import random 
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.db import migrations
from django.utils.timezone import datetime
from django.utils import timezone


app = 'innovation_module'

def make_migrations(apps, schema_editor):
    create_status_pomyslu(apps)
    create_ustawienia_oceniania(apps)
    create_slowo_kluczowe(apps)
    create_uzytkownik(apps)
    create_pomysl(apps)
    create_ocena(apps)
    create_rodzaj_decyzji(apps)
    create_watek(apps)
    create_post(apps)
    add_role_to_uzytkownik(apps)
    create_zalacznik(apps)


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

def create_slowo_kluczowe(apps):
    SlowoKluczowe = apps.get_model(app, 'SlowoKluczowe')

    slowo_kluczowe = ['Komputery i peryferia', 'Robotyka', 'Infrastruktura', 'Machine Learning', 'Rozrywka', 'Dydaktyka','Akademiki', 'Inne']

    for sk in slowo_kluczowe:
        m = SlowoKluczowe(slowo_kluczowe = sk)
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
    SlowoKluczowe = apps.get_model(app, 'SlowoKluczowe')

    ideas = [
        ('Nowe komputery', 'Zakup 4 komputerów o dużej mocy obliczeniowej, które dostepnę będą dla studentów', 'Możliwość wykorzystania lepszego i szybszego sprzętu podczas testowania czasochłonnych algorytmów w pracach dyplomowych i nie tylko.', 'Koszt komputerów to ok 60 000 złotych', '5'),
        ('Nowe drukarki', 'Zakup 5 drukarek i rozmieszczenie ich w kilku punktach budynku wydziału', 'Drukarki będa dostępne dla studentów na miejscu.', 'Koszty drukarek ok. 1500 złotych', '8'),
        ('Nowe wejście', 'Otworzenie dotąd nidostępnych drzwi wejściowych', 'Mniejsze tłoki przy wejściu głownym', 'brak', '7'),
        ('Nowe szatnie', 'Stworzenie niestrzeżonej szatni przy drógim wejściu', 'Szybsza obsługa. Mniejsze zagęszczenie osób przy szatni głównej wpływające na zmniejszenie ryzyka zakażenia koronawirusem ', 'Koszty 1000 złotych na adaptację pomieszczenia', '6'),
        ('Nowe stojaki na rowery', 'Umieszczenie przed bydynkiem wydziału 50 monitorowanych stojaków rowerowych', 'Studenci będą chętniej podróżowali rowerami na uczelnie co wpłynie korzystnie na ich zdrowie fizyczne', 'Koszt to ok. 4000 złotych ', '6'),
        ('Darmowe automaty do kawy', 'Zakup i utrzymanie dwóch automatów do kawy i umieszczenie ich przy dwóch wejściach ', 'Większość studentów jest zaspanych na porannych zjeciach. Wprowadzenie tego pomysłu może poprawić ich uwagę oraz pozytywnie wpłynąć na wyniki. Dodatkowo taki gest ociepli stosunek uczelni do swoich studentów ', 'Początkowy koszt 2000zl oraz koszt stały roczny ok. 1000zl', '10'),
        ('Rozbudowa przestrzeni studenckiej', 'Zakup nowych kanap, foteli stolików oraz ich rozmieszczenie w wolnych miejscach na korytarzu', 'Miejsca te zachęcą studentów do lepszego wykorzystania wolnych chwil pomiędzy zajęciami.', 'Koszt ok. 50 000 złotych ', '8'),
        ('Poprawa materiałów dydaktycznych', 'Zebranie oraz odświeżenie myśli dydaktycznej przekazywanej podczas wykładu w plik pdf udostępniany studentom jeśli wcześniej takie źródła nie istniały', 'Jeśli student nie będzie miał potrzeby notowania obfitych treści przekazywanych podczas wykładu będzie mógł bardziej skupić się na słuchaniu oraz aktywnym udziale w zajęciach  ', 'Koszty nie znane', '3'),
        ('Imprezy i Integracja', 'Organizowanie imprez integracyjnych i wydziałowych razem wydziałami z przeważającym udziałem studentek', 'Pozowli to na rozwój kompetencji miękkich wśród przeważającej liczby studentów wydziału oraz poprawi horyzonty o wiedzę nie czysto techniczną', 'Nie dotyczy', '6'),
        ('Turniej planszówek', 'Zorganizowanie przez wydział turnieju planszówek o puchar dziekana.', 'Rozwój zainteresowań studentów. Aktywacja życia studenckiego', 'Koszt ok 1000 złotych', '9')
    ]

    users = Uzytkownik.objects.all()
    # statuses = StatusPomyslu.objects.all()
    settings = UstawieniaOceniania.objects.all()

    slowo_kluczowe = SlowoKluczowe.objects.get(slowo_kluczowe='Komputery i peryferia')

    for i in ideas[0:2]:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')        
        setting = random.choice(settings[1:])

        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(1, 100))

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status_pomyslu=status, ustawienia_oceniania=setting, uzytkownik=user, slowo_kluczowe=slowo_kluczowe, data_dodania=date)
        m.save()

    slowo_kluczowe = SlowoKluczowe.objects.get(slowo_kluczowe='Inne')


    slowo_kluczowe = SlowoKluczowe.objects.get(slowo_kluczowe='Infrastruktura')

    for i in ideas[2:7]:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')        
        setting = random.choice(settings[1:])

        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(1, 100))

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status_pomyslu=status, ustawienia_oceniania=setting, uzytkownik=user, slowo_kluczowe=slowo_kluczowe, data_dodania=date)
        m.save()

    slowo_kluczowe = SlowoKluczowe.objects.get(slowo_kluczowe='Dydaktyka')

    for i in ideas[7:8]:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')        
        setting = random.choice(settings[1:])

        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(1, 100))

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status_pomyslu=status, ustawienia_oceniania=setting, uzytkownik=user, slowo_kluczowe=slowo_kluczowe, data_dodania=date)
        m.save()

    slowo_kluczowe = SlowoKluczowe.objects.get(slowo_kluczowe='Rozrywka')

    for i in ideas[8:10]:
        user = random.choice(users)
        # status = random.choice(statuses)
        status = StatusPomyslu.objects.get(status='Oczekujacy')        
        setting = random.choice(settings[1:])

        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(5, 100))

        m = Pomysl(tematyka=i[0], opis=i[1], planowane_korzysci=i[2], planowane_koszty=i[3],
                   ocena_wazona=i[4], status_pomyslu=status, ustawienia_oceniania=setting, uzytkownik=user, slowo_kluczowe=slowo_kluczowe, data_dodania=date)
        m.save()

def create_ocena(apps):
    Ocena = apps.get_model(app, 'Ocena')
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    Pomysl = apps.get_model(app, 'Pomysl')

    opinions = [
        ('2021-01-17 12:00:50', 9, 'Bardzo dobry pomysl'),
        ('2021-01-17 13:40:40', 9, 'Bardzo dobry pomysl'),
        ('2021-01-17 12:04:20', 6, 'Dobry pomysl'),
        ('2021-01-17 16:06:02', 6, 'Dobry pomysl'),
        ('2021-01-17 20:10:30', 2, 'Słaby pomysl'),
        ('2021-01-17 12:11:03', 2, 'Słaby pomysl'),
        ('2021-01-17 21:09:30', 8, 'Bardzo dobry pomysl'),
        ('2021-01-17 09:05:50', 7, 'Dobry pomysl'),
        ('2021-01-17 22:01:20', 1, 'Do kosza'),
        ('2021-01-17 23:55:09', 5, 'Przeciętny pomysl'),
    ]

    users = Uzytkownik.objects.all()
    ideas = Pomysl.objects.all()

    for opinion in opinions:
        idea = random.choice(ideas)
        user = random.choice([u for u in users if u is not idea.uzytkownik])

        settings = idea.ustawienia_oceniania.ustawienia

        m = Ocena(data=opinion[0], pomysl=idea, uzytkownik=user)

        if 'num' in settings:
            m.ocena_liczbowa = opinion[1]

        if 'text' in settings:
            m.opis = opinion[2]

        m.save()
    # Dodaanie ocen indywiduallnie
    #Dodanie opinni pomysł 1
    idea=ideas[0]
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-18 23:55:09', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 8

    if 'text' in settings:
        m.opis = 'Świetny pomysł. Z pewnością się przydadzą'
    m.save()
    
    #Dodanie opinni pomysł 2
    idea = Pomysl.objects.get(pk=2)
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-18 22:55:09', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 7

    if 'text' in settings:
        m.opis = 'Średni pomysł. Dużo punktów jest wokół uczelni. Ale tego nigdy zbyt wiele.'
    m.save()
    
    #Dodanie opinni pomysł 3
    idea = Pomysl.objects.get(pk=3)
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-18 19:05:09', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 2

    if 'text' in settings:
        m.opis = 'Nie popieram. Wiekszość użytecznych wejść jest już otwarta. Wszystkie nie powinny być otwarte ze względów bezpieczeństwa.'
    m.save()

    #Dodanie opinni pomysł 4
    idea = Pomysl.objects.get(pk=4)
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-18 18:05:09', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 7

    if 'text' in settings:
        m.opis = 'Ciekawa propozycja. Godna dalszego rozważenia'
    m.save()

    #Dodanie opinni pomysł 5
    idea = Pomysl.objects.get(pk=5)
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-17 10:05:09', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 10

    if 'text' in settings:
        m.opis = 'Super pomysł. Taki parking ze zwiększonym bezpieczeństwem zachęcił by wielu studentów do korzystania z niego'
    m.save()

    #Dodanie opinni pomysł 6
    idea = Pomysl.objects.get(pk=6)
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-17 14:55:19', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 7

    if 'text' in settings:
        m.opis = 'Ciekawy pomysł. Wielu studentów skusiłaby darmowa kawa.'
    m.save()

    #Dodanie opinni pomysł 9
    idea = ideas[8]
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-17 17:20:40', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 9

    if 'text' in settings:
        m.opis = 'Super pomysł. Z pewnością będzie się cieszył dużą popularnością wśród studentów'
    m.save()

    #Dodanie opinni pomysł 9
    idea = ideas[8]
    user = random.choice([u for u in users if u is not idea.uzytkownik])
    m = Ocena(data='2021-01-18 23:20:40', pomysl=idea, uzytkownik=user)
    if 'num' in settings:
        m.ocena_liczbowa = 10

    if 'text' in settings:
        m.opis = 'Warto rozważyć wejście w kooperację z wydziałami spoza Politechniki.'
    m.save()

def create_watek(apps):
    Watek = apps.get_model(app, 'Watek')

    threads = ['Nowe wyposażenie, które przydałoby się na uczelni', 'Dyski SSD', 'Rozrywka w czasie pandemii']

    for thread in threads:
        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(30, 50))
        last_date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(1, 30))
        m = Watek(temat=thread, data_dodania =date, data_ostatniego_posta = last_date)
        m.save()
    
def create_post(apps):
    Post = apps.get_model(app, 'Post')
    Uzytkownik = apps.get_model(app, 'Uzytkownik')
    Watek = apps.get_model(app, 'Watek')

    posts = [
        ('Tytul 1', 'Fajnie by było mieć wiecej openspacu. Jakieś kanapy itp.'),
        ('Tytul 2', 'O do tego przydałyby się dodatkowe stoliki gdzie można posiedzieć z komputerem a nie trzymać go na kolanach'),
        ('Tytul 3', 'Świetny pomysł. Szczególnie na parterze.'),
        ('Tytul 4', 'Poleca ktoś jakiś dysk SSD do komputera na M2 w fajnej cenia?'),
        ('Tytul 5', 'Obczaj sobie Cruciala MX500. Na x-kom są nieraz fajne promki.'),
        ('Tytul 6', 'Fajna, budżetowa opcja jeśli nie masz ogromnych wymagań co do szybkości.'),
        ('Tytul 7', 'To takie coś istnieje? No dobra nie jest tak źle. W sumie ja nie widze różnicy przed i po.'),
        ('Tytul 8', 'Zawsze można iśc na domówkę w małym gronie '),
        ('Tytul 9', 'Albo grać więcej w gry xd '),
    ]

    users = Uzytkownik.objects.all()
    threads = Watek.objects.all()

    # for post in posts:
    #     user = random.choice(users)
    #     thread = random.choice(threads)
    #     date = thread.data_ostatniego_posta

    #     m = Post(tytul=post[0], tresc=post[1], watek = thread, uzytkownik= user,data_dodania=date)
    #     m.save()
    #pierwszy thread
    user = users[0]
    thread = threads[0]
    date = thread.data_ostatniego_posta - timedelta(days=1)
    m = Post(tytul=posts[0][0], tresc=posts[0][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[2]
    date = date+timedelta( minutes=33 )
    m = Post(tytul=posts[1][0], tresc=posts[1][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[5]
    date = thread.data_ostatniego_posta
    m = Post(tytul=posts[2][0], tresc=posts[2][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()

    #Drugi thread
    user = users[3]
    thread = threads[1]
    date = thread.data_ostatniego_posta-timedelta(minutes=300)
    m = Post(tytul=posts[3][0], tresc=posts[3][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[7]
    date = date+timedelta( seconds=1000 )
    m = Post(tytul=posts[4][0], tresc=posts[4][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[9]
    date = thread.data_ostatniego_posta
    m = Post(tytul=posts[5][0], tresc=posts[5][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()

    #Trzeci thread
    user = users[8]
    thread = threads[2]
    date = thread.data_ostatniego_posta-timedelta(minutes=400)
    m = Post(tytul=posts[3][0], tresc=posts[3][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[1]
    date = date+timedelta( seconds=2000 )
    m = Post(tytul=posts[4][0], tresc=posts[4][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()
    user = users[6]
    date = thread.data_ostatniego_posta
    m = Post(tytul=posts[5][0], tresc=posts[5][1], watek = thread, uzytkownik= user,data_dodania=date)
    m.save()


def create_zalacznik(apps):
    Zalacznik = apps.get_model(app, 'Zalacznik')
    Pomysl = apps.get_model(app, 'Pomysl')
    Post = apps.get_model(app, 'Post')
    ZalacznikPomyslu = apps.get_model(app, 'ZalacznikPomyslu')
    ZalacznikPosta = apps.get_model(app, 'ZalacznikPosta')

    zalaczniki = [
        ('file1.txt', 1),
        ('img1.jpg', 2),
        ('file2.txt', 3),
        ('img2.jpg', 2)
    ]

    for z in zalaczniki:
        date = timezone.localtime(timezone.now()) - timedelta(days=random.randint(1, 100))
        m = Zalacznik(nazwa_pliku=z[0], rozmar=z[1], data_dodania=date)
        m.save()

    attachments = Zalacznik.objects.all()

    for i in range(2):
        m = ZalacznikPomyslu(zalacznik = attachments[i], pomysl=Pomysl.objects.get(pk=i+1))
        m.save()
    
    for i in range(2, 4):
        m = ZalacznikPosta(zalacznik = attachments[i], post=Post.objects.get(pk=i-1))
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        (app, '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_migrations)
    ]