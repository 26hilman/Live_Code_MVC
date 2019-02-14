from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampilan_toko, name='toko'),
    path('barang/tambah', views.input_post, name='tambah'),
    path('barang/<int:toko_id>', views.toko_detail, name='toko_detail'),
]