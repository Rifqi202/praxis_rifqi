from django.shortcuts import redirect, render
from . import models

# Create your views here.
def minuman(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST["nama"]
        input_harga = request.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(request, "indexminum.html", {
        "data": data,
    })
def hapus(request, id):
    models.minuman.objects.filter(id = id).delete()
    return redirect('/minuman/')
def edit(request, id):
    if request.POST:
        input = request.POST["nama"]
        print(input)
        models.minuman.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.minuman.objects.filter(id = id).first()
    return render(request,"editminum.html",{
        "detailData" : data,
    })
def detail(request, id):
    data = models.minuman.objects.filter(id = id).first()
    print(data)
    return render(request, "detailminum.html", {
        "detailData": data,
    })
