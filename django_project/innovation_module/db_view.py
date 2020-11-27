from . import models
from django.core import serializers
import json

def serialize(objects):
    raw = serializers.serialize('python', objects)
    return json.dumps([o['fields'] for o in raw])

def get_ideas(user = None):
    if user is None:
        return models.Pomysl.objects.all()
    
    return models.Pomysl.objects.get(user=user)

def get_ideas_json(user=None):
    return serialize(get_ideas(user))

