

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
 
# Table Data Satuan
class msatuan(models.Model): 
    kode_satuan = models.CharField(max_length=4, primary_key=True)
    nama_satuan = models.CharField(max_length=50)
    nama_singkat = models.CharField(max_length=100)
    usertime =models.DateTimeField(auto_now=True)
 
class mdafsat(models.Model):
    kode_daftar_satuan = models.CharField(max_length=4, primary_key=True)
    satuan_terbesar =models.CharField(max_length=100)
    satuan_sedang = models.CharField(max_length=100)
    satuan_terkecil = models.CharField(max_length=100)
    jumsat_terbesar = models.CharField(max_length=50)
    jumsat_sedang = models.CharField(max_length=50)
    jumsat_terkecil = models.CharField(max_length=50)
       
class mbarang(models.Model):
    kode_barang = models.CharField(max_length=4, primary_key=True)
    nama_barang_lengkap = models.CharField(max_length=100)
    nama_barang_penjualan = models.CharField(max_length=100)
    jenis_barang = models.CharField(max_length=100)
    satua_terkecil = models.CharField(max_length=50)
    barcode_terkecil = models.CharField(max_length=20)
    harga_pl_sebelum_ppn = models.CharField(max_length=100)
    harga_pl_sesudah_ppn = models.CharField(max_length=100)
    harga_pokok_penjualan = models.CharField(max_length=100)
    margin_penjualan = models.CharField(max_length=50)
    harga_penjualan_sat_terkecil = models.CharField(max_length=100)
    tanggal_update_terakhir =  models.DateTimeField(auto_now=True)
    kode_dafar_satuan = models.CharField(max_length=4)
    status_aktif_barang = models.CharField(max_length=1,default="y")
    usertime = models.DateTimeField(auto_now=True)
    
class admin(models.Model):
    id_admin = models.CharField(max_length=4, primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    telepon = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
     