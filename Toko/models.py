from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models

# Create your models here.
class Toko(models.Model):
    gambar = models.ImageField(upload_to = 'images')
    nama_barang = models.CharField(max_length=255)
    harga = models.CharField(max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_barang