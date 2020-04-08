from django.shortcuts import render
from .models import Img
from django.conf import settings
from django.http import HttpResponse
import os


# Create your views here.

def upload(request):
    obj = {}
    if request.method == 'POST':
        files = request.FILES.getlist('pics',None)
        if not files:
            obj['error'] = '没有上传的文件！'
        else:
            dirs = settings.MEDIA_ROOT + '/img/'
            folder = os.path.exists(dirs)
            if not folder:
                os.makedirs(dirs)
            try:
                for item in files:
                    pic = Img(img=item)
                    pic.save()
                    res = pic
            except Exception as e:
                obj['error'] = e
    #return render(request, 'upload_materials/upload.html')
    return render(request, 'upload_materials/upload.html')

def show(request):
    imgs = Img.objects.all()
    content = {'imgs':imgs,
            }
    for i in imgs:
        print(i.img.url)
    return render(request,'upload_materials/show.html',content)
