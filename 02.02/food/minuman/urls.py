from django.urls import path


from . import views

urlpatterns = [
    path('', views.minuman, name='minuman'),
    path('minuman/', views.minuman, name='minuman'),
    path('hapus/<id>', views.hapus),
    path('edit/<id>/', views.edit),
    path('detail/<id>/', views.detail),
]