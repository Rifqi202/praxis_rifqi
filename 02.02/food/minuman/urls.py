from django.urls import path


from . import views

urlpatterns = [
    path('', views.minuman, name='minuman'),
    path('minuman/', views.minuman, name='minuman'),
    path('minuman/hapus/<id>', views.hapus),
    path('minuman/edit/<id>/', views.edit),
    path('minuman/detail/<id>/', views.detail),
]