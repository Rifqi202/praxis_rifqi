from django.db import models
from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(request):
    if request.POST:
        models.makanan.objects.create(
            jenis = request.POST["jenis"],
            nama = request.POST["nama"],
            harga = request.POST["harga"]
            )
        return redirect('/')
    data = models.makanan.objects.all()
    return render(request, "index.html", {
        "data":data,
    })

def makanan(request):
     if request.POST:
         input_jenis = request.POST["jenis"]
         input_nama = request.POST["nama"]
         input_harga = request.POST["harga"]
         models.makanan.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
     data = models.makanan.objects.all()
     return render(request, "index.html", {
         "data": data,
     })
def hapus(request, id):
         models.makanan.objects.filter(id = id).delete()
         return redirect('/')
     
def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print (input)
        models.makanan.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.makanan.objects.filter(id = id).first()
    return render(request,"edit.html", {
        "datailData" : data,
    })

def detail(request, id):
     data = models.makanan.objects.filter(id = id).first()
     print(data)
     return render(request,"detail.html", {
         "detail.data" : data,
     })

    