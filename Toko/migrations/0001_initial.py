# Generated by Django 2.1.7 on 2019-02-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='images')),
                ('nama_barang', models.CharField(max_length=255)),
                ('harga', models.CharField(max_length=50)),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
