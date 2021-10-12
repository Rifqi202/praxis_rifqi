from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('makanan/', views.Makanan, name='Makanan'),
    # path('hapus/<id>', views.hapus),
     path('edit/<id>', views.edit),
    # path('detail/<id>/', views.detail),

]
