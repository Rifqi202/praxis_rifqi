from django.urls import path

from . import views

urlpatterns = [
    path('', views.pesanan, name = 'pesanan'),
    path('pesanan/', views.pesanan, name = 'pesanan'),
    path('hapus/<id>', views.hapus),
    path('edit/<id>/', views.edit),
    path('detail/<id>/', views.detail),
]