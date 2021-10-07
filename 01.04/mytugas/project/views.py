from django.db import models
from django.shortcuts import render
from . import models
from django.http import HttpResponse


def index(request):
    if request.POST:

        #input data ke database
        models.project.objects.create(nama = request.POST['fname'])
    #nampilin data
    data2 =models.project.objects.all()

    return render(request, 'index.html', {'isi': data2})

def about(request):
    return HttpResponse("Halaman about")



    