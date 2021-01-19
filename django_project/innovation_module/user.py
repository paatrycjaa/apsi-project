import json

from django.core.serializers.json import DjangoJSONEncoder

from . import models

def get_user_data(user):
    uzytkownik = models.Uzytkownik.objects.get(user=user)

    data = {
        'firstName': uzytkownik.imie,
        'lastName': uzytkownik.nazwisko,
    }

    if models.Administrator.objects.filter(uzytkownik=uzytkownik).exists():
        data['role'] = 'Administrator'
    elif models.CzlonekKomisji.objects.filter(uzytkownik=uzytkownik).exists():
        data['role'] = 'Członek Komisji'
    else:
        data['role'] = 'Użytkownik'

    return json.dumps(data, cls=DjangoJSONEncoder)