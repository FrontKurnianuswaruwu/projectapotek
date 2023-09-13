from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kelompok,mapotik,mjenis,msatuan,mdafsat
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    context= {
        'name':'front'
    }
    return render(request,'index.html',context)

def index2(request):
    return render(request,'index2.html')

def dashboard(request):
    return render(request,'dashboard.html')

#Table Kelompok Barang
def tambahmkelompok(request):
    return render(request,'tambah-kelompok-barang.html')

def tambahkelompokpost(request):
    nama_kelompok = request.POST['nama_kelompok']
    
    # Ambil huruf pertama dari nama_kelompok
    first_letter = nama_kelompok[0].upper()
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_kelompok = Kelompok.objects.filter(kode_kelompok__startswith=first_letter)
    # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_kelompok.filter(kode_kelompok=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    kode_kelompok = first_letter + str(number).zfill(3)
    
    # jika ada kode kelompok yang sama maka akan ada pesan error
    if Kelompok.objects.filter(kode_kelompok=kode_kelompok).exists():
        messages.error(request, 'Kode Kelompok Sudah Digunakan')
    
    # proses jika benar 
    else:
        tambah_kode_kelompok = Kelompok(
            kode_kelompok=kode_kelompok,
            nama_kelompok=nama_kelompok,
        )
        tambah_kode_kelompok.save()
        messages.success(request, 'BERHASIL TAMBAH KELOMPOK')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def mastermkelompok(request):
    data_mkelompok = Kelompok.objects.all()
    context = {
        'data_mkelompok' : data_mkelompok
    }
    return render (request,'master-mkelompok.html',context)

def updatmkelompok(request, kode_kelompok):
    data_mkelompok = Kelompok.objects.get(kode_kelompok=kode_kelompok)
    context = {
        'data_mkelompok': data_mkelompok
    }
    return render(request, 'update-mkelompok.html', context)    

def postupdatemkelompok(request):
    # ambil data dari POST
    kode_kelompok = request.POST['kode_kelompok']
    nama_kelompok = request.POST['nama_kelompok']
    usertime = request.POST['usertime']
    
    #proses update
    #ngambil data 
    data_mkelompok = Kelompok.objects.get(kode_kelompok=kode_kelompok)
    data_mkelompok.kode_kelompok = kode_kelompok
    data_mkelompok.nama_kelompok = nama_kelompok
    data_mkelompok.usertime = usertime
    #simpan ke tabel
    data_mkelompok.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def deletemkelompok(request, kode_kelompok):
    Kelompok.objects.get(kode_kelompok=kode_kelompok).delete()
    messages.success(request, 'BERHASIL HAPUS')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Kelompok Barang

#Table Perusahaan Apotik
def add(request):
    return render(request,'mkelompok/add-kel-brg')

def postadd(request):
    nama_apotik = request.POST['nama_apotik']
    alamat_apotik = request.POST['alamat_apotik']
    telepon_retail = request.POST['telepon_retail']
    owner = request.POST['owner']
    kontak_person = request.POST['kontak_person']

    data_mapotik = mapotik(
        nama_apotik = nama_apotik,
        alamat_apotik = alamat_apotik,
        telepon_retail = telepon_retail,
        owner = owner,
        kontak_person = kontak_person,
    )
    data_mapotik.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def v(request):
    data_mapotik = mapotik.objects.all()
    context = {
        'data_mapotik' : data_mapotik
    }
    return render(request,'mkelompok/v-kel-brg.html', context)

def up(request, id):
    data_mapotik = mapotik.objects.get(id = id)
    context = {
        'data_mapotik' : data_mapotik
    }
    return render(request, 'mkelompok/up-kel-brg.html', context)

def postup(request):
    id = request.POST['id']
    nama_apotik = request.POST['nama_apotik']
    alamat_apotik = request.POST['alamat_apotik']
    telepon_retail = request.POST['telepon_retail']
    owner = request.POST['owner']
    kontak_person = request.POST['kontak_person']

    data_mapotik = mapotik.objects.get( id=id)
    data_mapotik.id = id
    data_mapotik.nama_apotik = nama_apotik
    data_mapotik.alamat_apotik = alamat_apotik
    data_mapotik.telepon_retail = telepon_retail
    data_mapotik.owner = owner
    data_mapotik.kontak_person = kontak_person

    data_mapotik.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Perusahaan Apotik

#Table Jenis Barang
def addmjenis(request):
    kode_mkelompok = Kelompok.objects.filter()
    context = {
        'kode_mkelompok' : kode_mkelompok
    }
    return render(request, 'mjenis/add-kel-brg.html', context)

def postaddmjenis(request):
    nama_jenis = request.POST['nama_jenis']
    kode_kelompok = request.POST['kode_kelompok']
    Status_ppn = request.POST['Status_ppn']

    # Ambil huruf pertama dari nama_kelompok
    first_letter = nama_jenis[0].upper()
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_jenis = mjenis.objects.filter(kode_jenis__startswith=first_letter)
    # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_jenis.filter(kode_jenis=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    kode_jenis = first_letter + str(number).zfill(3)
    
    # jika ada kode kelompok yang sama maka akan ada pesan error
    

    tambah_mjenis = mjenis(
        kode_jenis = kode_jenis,
        kode_kelompok = kode_kelompok,
        nama_jenis =nama_jenis,
        status_ppn = Status_ppn,
    )
    tambah_mjenis.save()
    messages.success(request, 'BERHASIL TAMBAH JENIS BARANG')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def vmjenis(request):
    data_mjenis = mjenis.objects.all()
    context = {
        'data_mjenis' : data_mjenis
    }
    return render(request, 'mjenis/v-jenis-brg.html', context)
    
def upmjenis(request, kode_jenis):
    data_mjenis = mjenis.objects.get(kode_jenis = kode_jenis)
    kode_mkelompok = Kelompok.objects.filter()
    context = {
        'data_mjenis' : data_mjenis,
        'kode_mkelompok' : kode_mkelompok
    }
    return render(request, 'mjenis/up-jenis-brg.html',context)

def postupmjenis(request):
    kode_jenis = request.POST['kode_jenis']
    nama_jenis = request.POST['nama_jenis']
    kode_kelompok = request.POST['kode_kelompok']
    status_ppn = request.POST['status_ppn']
    usertime = request.POST['usertime']

    data_mjenis = mjenis.objects.get(kode_jenis=kode_jenis)
    data_mjenis.kode_jenis = kode_jenis
    data_mjenis.nama_jenis = nama_jenis
    data_mjenis.kode_kelompok = kode_kelompok
    data_mjenis.status_ppn = status_ppn
    data_mjenis.usertime = usertime

    data_mjenis.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delmjenis(request, kode_jenis):
    mjenis.objects.get(kode_jenis=kode_jenis).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Jenis Barang

#Table Data Satuan
def addmsatuan(request):
    return render(request,'msatuan/add-satuan-brg.html')

def postaddmsatuan(request):
    nama_satuan = request.POST['nama_satuan']
    nama_singkat = request.POST['nama_singkat']
    
     # Ambil huruf pertama dari nama_kelompok
    first_letter = nama_satuan[0].upper()
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_jenis = msatuan.objects.filter(kode_satuan__startswith=first_letter)
    # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_jenis.filter(kode_satuan=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    kode_satuan = first_letter + str(number).zfill(3)
    
    # jika ada kode kelompok yang sama maka akan ada pesan error
    
    data_msatuan = msatuan(
        kode_satuan =kode_satuan,
        nama_satuan = nama_satuan,
        nama_singkat = nama_singkat,  
    )
    data_msatuan.save()
    messages.success(request, 'BERHASIL TAMBAH JENIS BARANG')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def vmsatuan(request):
    data_msatuan = msatuan.objects.all()
    context = {
        'data_msatuan' : data_msatuan
    }    
    return render(request, 'msatuan/v-satuan-brg.html',context)
    
def upmsatuan(request, kode_satuan):
    data_msatuan = msatuan.objects.get(kode_satuan=kode_satuan)
    context = {
        'data_msatuan' : data_msatuan
    }    
    return render(request, 'msatuan/up-satuan-brg.html',context)
    
def postupmsatuan(request):
    kode_satuan = request.POST['kode_satuan']
    nama_satuan = request.POST['nama_satuan']
    nama_singkat = request.POST['nama_singkat']
    usertime = request.POST['usertime']
    
    data_msatuan = msatuan.objects.get(kode_satuan=kode_satuan)
    data_msatuan.kode_satuan = kode_satuan
    data_msatuan.nama_satuan = nama_satuan
    data_msatuan.nama_singkat = nama_singkat
    data_msatuan.usertime = usertime
    
    data_msatuan.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delmsatuan(request , kode_satuan):
    msatuan.objects.get(kode_satuan=kode_satuan).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Data Satuan

#Table Satuan Bertingkat
def addmdafsat(request):
    return render(request, 'mdafsat/add-mdafsat-brg.html') 

def postaddmdafsat(request):
    satuan_terbesar = request.POST['satuan_terbesar']
    satuan_sedang = request.POST['satuan_sedang']
    satuan_terkecil = request.POST['satuan_terkecil']
    jumsat_terbesar = request.POST['jumsat_terbesar']
    jumsat_sedang = request.POST['jumsat_sedang']
    jumsat_terkecil = request.POST['jumsat_terkecil']
    
      # Ambil huruf pertama dari nama_kelompok
    first_letter = satuan_terbesar[0].upper()
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_jenis = mdafsat.objects.filter(kode_daftar_satuan__startswith=first_letter)
    # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_jenis.filter(kode_daftar_satuan=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    kode_daftar_satuan = first_letter + str(number).zfill(3)
    
    data_mdafsat = mdafsat(
        kode_daftar_satuan = kode_daftar_satuan,
        satuan_terbesar =satuan_terbesar,
        satuan_sedang = satuan_sedang,
        satuan_terkecil = satuan_terkecil,
        jumsat_terbesar = jumsat_terbesar,
        jumsat_sedang = jumsat_sedang,
        jumsat_terkecil = jumsat_terkecil,
    )
    data_mdafsat.save()
    messages.success(request, 'BERHASIL TAMBAH JENIS BARANG')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def vmdafsat(request):
    data_mdafsat = mdafsat.objects.all()
    context = {
        'data_mdafsat' : data_mdafsat
    }
    return render(request, 'mdafsat/v-dafsat-brg.html',context)

def upmdafsat(request, kode_daftar_satuan) :
    data_mdafsat = mdafsat.objects.get(kode_daftar_satuan = kode_daftar_satuan)
    context = {
        'data_mdafsat' :data_mdafsat
    }  
    return render(request, 'mdafsat/up-mdafsat-brg.html',context)

def postupmdafsat(request):
    kode_daftar_satuan = request.POST['kode_daftar_satuan']
    satuan_terbesar = request.POST['satuan_terbesar']
    satuan_sedang = request.POST['satuan_sedang']
    satuan_terkecil = request.POST['satuan_terkecil']
    jumsat_terbesar = request.POST['jumsat_terbesar']
    jumsat_sedang = request.POST['jumsat_sedang']
    jumsat_terkecil = request.POST['jumsat_terkecil']
    
    data_mdafsat = mdafsat.objects.get(kode_daftar_satuan=kode_daftar_satuan)
    data_mdafsat.kode_daftar_satuan = kode_daftar_satuan
    data_mdafsat.satuan_terbesar = satuan_terbesar
    data_mdafsat.satuan_sedang = satuan_sedang
    data_mdafsat.satuan_terkecil = satuan_terkecil
    data_mdafsat.jumsat_terbesar = jumsat_terbesar
    data_mdafsat.jumsat_sedang = jumsat_sedang
    data_mdafsat.jumsat_terkecil = jumsat_terkecil
    
    data_mdafsat.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delmdafsat(request, kode_daftar_satuan):
    mdafsat.objects.get(kode_daftar_satuan=kode_daftar_satuan).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Satuan Bertingkat
    
        
    
    
    