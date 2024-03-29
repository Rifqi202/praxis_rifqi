from django.shortcuts import render, redirect
from . import models

# Create your views here.
def pesanan(request):
    if request.POST:
        get_makanan = request.POST["makanan"]
        get_minuman = request.POST["minuman"]
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman = request.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id = get_makanan).first()
        input_minuman = models.minuman.objects.filter(id = get_minuman).first()
        models.pesanan.objects.create(makanan = input_makanan, minuman = input_minuman, jumlah_makanan = get_jumlah_makanan, jumlah_minuman = get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "indexpesan.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data" : data,

    })
def hapus(request, id):
    models.pesanan.objects.filter(id = id).delete()
    return redirect("/pesanan/")
def edit(request, id):
    if request.POST:
        get_makanan = request.POST["makanan"]
        get_minuman = request.POST["minuman"]
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman = request.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id = get_makanan).first()
        input_minuman = models.minuman.objects.filter(id = get_minuman).first()
        models.pesanan.objects.filter(id = id).update(makanan = input_makanan, minuman = input_minuman, jumlah_makanan = get_jumlah_makanan, jumlah_minuman = get_jumlah_minuman)
        return redirect("/pesanan/")
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.filter(id = id).first()
    return render(request, "editpesan.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })
def detail(request, id):
    data = models.pesanan.objects.filter(id = id).first()
    print(data)
    return render(request, "detailpesan.html",{
        "dataDetail": data,
    })