from typing import ValuesView
from django.db import models
from django.shortcuts import redirect, render
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

def hapus(request,id):
    models.project.objects.filter(pk = id).delete()
    return redirect('/')
def edit(request,id):
    if request. POST:
        input = request.POST["fname"]
        print(input)
        models.project.objects.filter(pk = id).update(nama = input)
        return redirect('/')
    data = models.project.objects.filter(pk = id).first()
    return render(request, "edit.html" , {
        "detailData": data,
    })
    
def detail(request, id):
    data = models.project.objects.filter()    
