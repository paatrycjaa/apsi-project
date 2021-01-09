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

            # with open(file_path, 'rb') as fh:
            #     response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            #     response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            #     return response