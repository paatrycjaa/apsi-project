import os 
import shutil 

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.http import FileResponse
from django.utils import timezone
import tempfile

from . import models

def download_file(file_id):
    try:
        file_name = models.Zalacznik.objects.get(pk=file_id).nazwa_pliku
        file_path = os.path.join(settings.MEDIA_ROOT, str(file_id) + '_' + file_name)        
        with tempfile.TemporaryDirectory(dir=settings.MEDIA_ROOT) as temp:                    
            tmp_path = os.path.join(temp, file_name)            
            shutil.copy(file_path, tmp_path)            
            if os.path.exists(tmp_path):
                return FileResponse(open(tmp_path, 'rb'), as_attachment=False)
    except:
        pass
    
    return HttpResponseNotFound("File not found.")

def save_file(file, file_name, attachment_pk):
    file_path = os.path.join(settings.MEDIA_ROOT, str(attachment_pk) + '_' + file_name)
    with open(file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

def add_idea_attachment(idea, file_name, flie_size):
    z = models.Zalacznik(nazwa_pliku=file_name, data_dodania=timezone.localtime(timezone.now()), rozmar=flie_size)
    z.save()
    
    zp = models.ZalacznikPomyslu(pomysl=idea, zalacznik=z)
    zp.save()

    return z.pk

def add_post_attachment(post, file_name, file_size):
    z = models.Zalacznik(nazwa_pliku=file_name, data_dodania=timezone.localtime(timezone.now()), rozmar=file_size)
    z.save()
    
    zp = models.ZalacznikPosta(post=post, zalacznik=z)
    zp.save()

    return z.pk