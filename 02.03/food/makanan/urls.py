from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('makanan/', views.makanan, name='makanan'),
     path('hapus/<id>', views.hapus),
     path('edit/<id>', views.edit),
     path('detail/<id>/', views.detail),

]
