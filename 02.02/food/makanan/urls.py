from django.urls import path

from . import views

urlpatterns = [
    # path('', views.makanan, name='makanan'),
    path('makanan/', views.makanan, name='makanan'),
    path('makanan/hapus/<id>', views.hapus),
    path('makanan/edit/<id>/', views.edit),
    path('makanan/detail/<id>/', views.detail),

]
