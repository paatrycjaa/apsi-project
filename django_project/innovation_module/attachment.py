import os 

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.http import FileResponse

from . import models

def download_file(file_id):
    try:
        file_name = models.Zalacznik.objects.get(pk=file_id).nazwa_pliku
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
             return FileResponse(open(file_path, 'rb'))
    except:
        pass
    
    return HttpResponseNotFound("File not found.")

def save_file(file, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

def add_idea_attachment(idea, file_name):
    pass
