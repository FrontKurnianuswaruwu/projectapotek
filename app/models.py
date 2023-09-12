

from django.db import models

class Kelompok(models.Model):
    kode_kelompok = models.CharField(max_length=4, primary_key=True)
    nama_kelompok = models.CharField(max_length=30)
    usertime = models.DateTimeField(auto_now=True)

class mapotik(models.Model):
    id = models.AutoField(primary_key=True)
    nama_apotik = models.CharField(max_length=100)
    alamat_apotik = models.CharField(max_length=200)
    telepon_retail = models.CharField(max_length=20)
    owner = models.CharField(max_length=50)
    kontak_person = models.CharField(max_length=40)

class mjenis(models.Model):
    kode_jenis = models.CharField(max_length=4, primary_key=True)
    nama_jenis = models.CharField(max_length=100)
    kode_kelompok = models.CharField(max_length=4)
    status_ppn = models.CharField(max_length=20)
    usertime = models.DateTimeField(auto_now=True)
    
