from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kelompok,mapotik,mjenis,msatuan,mdafsat,admin,mprofil,mbarang
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .decorators import login_required

# Create your views here.
@login_required()
def index(request):
    context= {
        'name':'front'
    }
    return render(request,'index.html',context)

@login_required()
def index2(request):
    return render(request,'index2.html')

@login_required()
def dashboard(request):
    return render(request,'dashboard.html')

#Table Kelompok Barang
@login_required()
def tambahmkelompok(request):
    return render(request,'tambah-kelompok-barang.html')

@login_required()
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

@login_required()
def mastermkelompok(request):
    data_mkelompok = Kelompok.objects.all()
    context = {
        'data_mkelompok' : data_mkelompok
    }
    return render (request,'master-mkelompok.html',context)

@login_required()
def updatmkelompok(request, kode_kelompok):
    data_mkelompok = Kelompok.objects.get(kode_kelompok=kode_kelompok)
    context = {
        'data_mkelompok': data_mkelompok
    }
    return render(request, 'update-mkelompok.html', context)    

@login_required()
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

@login_required()
def deletemkelompok(request, kode_kelompok):
    Kelompok.objects.get(kode_kelompok=kode_kelompok).delete()
    messages.success(request, 'BERHASIL HAPUS')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Kelompok Barang

#Table Perusahaan Apotik
@login_required()
def add(request):
    return render(request,'mkelompok/add-kel-brg')

@login_required()
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

@login_required()
def v(request):
    data_mapotik = mapotik.objects.all()
    context = {
        'data_mapotik' : data_mapotik
    }
    return render(request,'mkelompok/v-kel-brg.html', context)

@login_required()
def up(request, id):
    data_mapotik = mapotik.objects.get(id = id)
    context = {
        'data_mapotik' : data_mapotik
    }
    return render(request, 'mkelompok/up-kel-brg.html', context)

@login_required()
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
@login_required()
def addmjenis(request):
    kode_mkelompok = Kelompok.objects.filter()
    context = {
        'kode_mkelompok' : kode_mkelompok
    }
    return render(request, 'mjenis/add-kel-brg.html', context)

@login_required()
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

@login_required()
def vmjenis(request):
    data_mjenis = mjenis.objects.all()
    context = {
        'data_mjenis' : data_mjenis
    }
    return render(request, 'mjenis/v-jenis-brg.html', context)

@login_required()   
def upmjenis(request, kode_jenis):
    data_mjenis = mjenis.objects.get(kode_jenis = kode_jenis)
    kode_mkelompok = Kelompok.objects.filter()
    context = {
        'data_mjenis' : data_mjenis,
        'kode_mkelompok' : kode_mkelompok
    }
    return render(request, 'mjenis/up-jenis-brg.html',context)

@login_required()
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

@login_required()
def delmjenis(request, kode_jenis):
    mjenis.objects.get(kode_jenis=kode_jenis).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Jenis Barang

#Table Data Satuan
@login_required()
def addmsatuan(request):
    return render(request,'msatuan/add-satuan-brg.html')

@login_required()
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

@login_required()
def vmsatuan(request):
    data_msatuan = msatuan.objects.all()
    context = {
        'data_msatuan' : data_msatuan
    }    
    return render(request, 'msatuan/v-satuan-brg.html',context)
   
@login_required() 
def upmsatuan(request, kode_satuan):
    data_msatuan = msatuan.objects.get(kode_satuan=kode_satuan)
    context = {
        'data_msatuan' : data_msatuan
    }    
    return render(request, 'msatuan/up-satuan-brg.html',context)

@login_required()  
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

@login_required()
def delmsatuan(request , kode_satuan):
    msatuan.objects.get(kode_satuan=kode_satuan).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Data Satuan

#Table Satuan Bertingkat
@login_required()
def addmdafsat(request):
    return render(request, 'mdafsat/add-mdafsat-brg.html') 

@login_required()
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

@login_required()
def vmdafsat(request):
    data_mdafsat = mdafsat.objects.all()
    context = {
        'data_mdafsat' : data_mdafsat
    }
    return render(request, 'mdafsat/v-dafsat-brg.html',context)

@login_required()
def upmdafsat(request, kode_daftar_satuan) :
    data_mdafsat = mdafsat.objects.get(kode_daftar_satuan = kode_daftar_satuan)
    context = {
        'data_mdafsat' :data_mdafsat
    }  
    return render(request, 'mdafsat/up-mdafsat-brg.html',context)

@login_required()
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

@login_required()
def delmdafsat(request, kode_daftar_satuan):
    mdafsat.objects.get(kode_daftar_satuan=kode_daftar_satuan).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
#End Table Satuan Bertingkat

#Data Barang
@login_required()
def addmbarang(request):
    data_mjenis = mjenis.objects.all()
    data_mdafsat = mdafsat.objects.all()
    context = {
        'data_mjenis' : data_mjenis,
        'data_mdafsat' : data_mdafsat
    }
    return render(request, 'mbarang/add-mbarang-brg.html',context)

def postaddmbarang(request):
    nama_barang_lengkap = request.POST["nama_barang_lengkap"]
    nama_barang_penjualan = request.POST['nama_barang_penjualan']
    jenis_barang = request.POST['jenis_barang']
    satua_terkecil = request.POST['satua_terkecil']
    barcode_terkecil = request.POST['barcode_terkecil']
    harga_pl_sebelum_ppn = request.POST['harga_pl_sebelum_ppn']
    harga_pl_sesudah_ppn = request.POST['harga_pl_sesudah_ppn']
    harga_pokok_penjualan = request.POST['harga_pokok_penjualan']
    margin_penjualan = request.POST['margin_penjualan']
    harga_penjualan_sat_terkecil = request.POST['harga_penjualan_sat_terkecil']
    kode_dafar_satuan = request.POST['kode_dafar_satuan']
    status_aktif_barang = request.POST['status_aktif_barang']
    
     # Ambil huruf pertama dari nama_kelompok
    first_letter = nama_barang_penjualan[0].upper()
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_jenis = mbarang.objects.filter(kode_barang__startswith=first_letter)
    # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_jenis.filter(kode_barang=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    kode_barang = first_letter + str(number).zfill(3)
    
    data_mbarang = mbarang(
        kode_barang = kode_barang ,
        nama_barang_lengkap = nama_barang_lengkap,
        nama_barang_penjualan = nama_barang_penjualan,
        jenis_barang = jenis_barang,
        satua_terkecil = satua_terkecil,
        barcode_terkecil = barcode_terkecil,
        harga_pl_sebelum_ppn = harga_pl_sebelum_ppn,
        harga_pl_sesudah_ppn = harga_pl_sesudah_ppn,
        harga_pokok_penjualan = harga_pokok_penjualan,
        margin_penjualan = margin_penjualan,
        harga_penjualan_sat_terkecil = harga_penjualan_sat_terkecil,
        kode_dafar_satuan = kode_dafar_satuan,
        status_aktif_barang = status_aktif_barang
    )
    data_mbarang.save()
    messages.success(request, 'BERHASIL TAMBAH BARANG')
    return redirect(request.META.get('HTTP_REFERER', '/'))
 
def vmbarang(request):
    data_mbarang = mbarang.objects.all()
    context = {
        'data_mbarang' : data_mbarang
    }
    return render(request, 'mbarang/v-mbarang-brg.html',context)

def upmbarang(request,kode_barang):
    data_mbarang = mbarang.objects.get(kode_barang=kode_barang)
    data_mjenis = mjenis.objects.all()
    data_mdafsat = mdafsat.objects.all()
    context = {
        'data_mbarang':data_mbarang,
        'data_mjenis' : data_mjenis,
        'data_mdafsat' : data_mdafsat
    }
    return render(request, 'mbarang/up-mbarang-brg.html',context)

def postupmbarang(request):
    kode_barang = request.POST['kode_barang']
    nama_barang_lengkap = request.POST['nama_barang_lengkap']
    nama_barang_penjualan = request.POST['nama_barang_penjualan']
    jenis_barang = request.POST['jenis_barang']
    satua_terkecil = request.POST['satua_terkecil']
    barcode_terkecil = request.POST['barcode_terkecil']
    harga_pl_sebelum_ppn = request.POST['harga_pl_sebelum_ppn']
    harga_pl_sesudah_ppn = request.POST['harga_pl_sesudah_ppn']
    harga_pokok_penjualan = request.POST['harga_pokok_penjualan']
    margin_penjualan = request.POST['margin_penjualan']
    harga_penjualan_sat_terkecil = request.POST['harga_penjualan_sat_terkecil']
    tanggal_update_terakhir = request.POST['tanggal_update_terakhir']
    kode_dafar_satuan = request.POST['kode_dafar_satuan']
    status_aktif_barang = request.POST['status_aktif_barang']
    usertime = request.POST['usertime']
    
    data_mbarang = mbarang.objects.get(kode_barang=kode_barang)
    data_mbarang.kode_barang = kode_barang
    data_mbarang.nama_barang_lengkap = nama_barang_lengkap
    data_mbarang.nama_barang_penjualan = nama_barang_penjualan
    data_mbarang.jenis_barang = jenis_barang
    data_mbarang.satua_terkecil = satua_terkecil
    data_mbarang.barcode_terkecil = barcode_terkecil
    data_mbarang.harga_pl_sebelum_ppn = harga_pl_sebelum_ppn
    data_mbarang.harga_pl_sesudah_ppn = harga_pl_sesudah_ppn
    data_mbarang.harga_pokok_penjualan = harga_pokok_penjualan
    data_mbarang.margin_penjualan = margin_penjualan
    data_mbarang.harga_penjualan_sat_terkecil = harga_penjualan_sat_terkecil
    data_mbarang.tanggal_update_terakhir = tanggal_update_terakhir
    data_mbarang.kode_dafar_satuan = kode_dafar_satuan
    data_mbarang.status_aktif_barang = status_aktif_barang
    data_mbarang.usertime = usertime
    
    data_mbarang.save()
    messages.success(request, 'BERHASIL UPDATE')
    return redirect('vmbarang')

def delmbarang (request, kode_barang):
    mbarang.objects.get(kode_barang=kode_barang).delete()
    messages.success(request, 'BERHASIL HAPUS DATA')
    return redirect(request.META.get('HTTP_REFERER', '/'))
    

#Admin
def addadmin(request):
    return render(request, 'madmin/add-admin-brg.html')

def postaddadmin(request):
    if request.method == 'POST':
        username = request.POST['username'].upper()
        password = request.POST['password'] 
        password_hash = make_password(password)
           # Ambil huruf pertama dari nama_kelompok
        first_letter = "A"
        # Cari semua kelompok yang memiliki huruf awal yang sama
        existing_jenis = admin.objects.filter(id_admin__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
        number = 1
        while existing_jenis.filter(id_admin=first_letter + str(number).zfill(3)).exists():
            number += 1
        # Setel kode_kelompok dengan format yang sesuai
        id_admin = first_letter + str(number).zfill(3)
        
  
        data_admin = admin(
            id_admin = id_admin,
            username = username,
            password = password_hash
        )
        data_admin.save()
        messages.success(request, 'BERHASIL REGISTER')
        return redirect('login')
        
def login(request):
    return render(request, 'madmin/l-admin-brg.html')

def logout(request):
    # hapus data session
    request.session.flush()
    messages.success(request, 'BERHASIL LOGOUT')
    return redirect('login')
def postllogin(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    
    if admin.objects.filter(username=username):
        data_admin = admin.objects.get(username=username)
        if password == password2:
            request.session['id_admin'] = data_admin.id_admin
            request.session['username'] = data_admin.username
            request.session.save()
            messages.success(request,'BERHASIL LOGIN')
            return redirect('vmprofil')
        else :
            messages.error(request, 'PASSWORD SALAH')
    else:
        messages.error(request,'ADMIN TIDAK DITEMUKAN')
    return redirect(request.META.get('HTTP_REFERER', '/'))            

def update(request, id_admin):
    data_admin = admin.objects.get(id_admin=id_admin)
    context = {
        'data_admin' : data_admin
    }
    return render(request, 'madmin/up-admin-brg.html', context)

@login_required()    
def postupadmin(request):
    id_admin = request.POST['id_admin']
    username = request.POST['username']
    email = request.POST['email']
    telepon = request.POST['telepon']
    
    data_admin = admin.objects.get(id_admin=id_admin)
    
    data_admin.id_admin = id_admin
    data_admin.username = username
    data_admin.email = email
    data_admin.telepon = telepon
    data_admin.save()
    messages.success(request,'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required()
def vadmin(request):
    data_admin = admin.objects.all()
    context = {
        'data_admin' : data_admin
    }    
    return render(request, 'madmin/v-admin-brg.html', context)
#End Admin  

#Mprofil
@login_required()
def addprofil(request):
    return render(request, 'mprofil/add-mprofil-brg.html')

@login_required()
def postaddmprofil(request):
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    gambar = request.FILES['gambar']
    facebook = request.POST['facebook']
    instagram = request.POST['instagram']
    email = request.POST['email']
    whatsapp = request.POST['whatsapp']
    
    first_letter = "P"
    # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_jenis = mprofil.objects.filter(id_apotik__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_jenis.filter(id_apotik=first_letter + str(number).zfill(3)).exists():
        number += 1
    # Setel kode_kelompok dengan format yang sesuai
    id_apotik = first_letter + str(number).zfill(3)
    
    data_mprofil = mprofil(
        id_apotik = id_apotik,
        nama = nama,
        alamat = alamat,
        gambar = gambar,
        facebook = facebook,
        instagram = instagram,
        email = email,
        whatsapp = whatsapp
    )
    data_mprofil.save()
    messages.success(request,'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required()
def vmprofil(request):
    data_mprofil = mprofil.objects.all()
    context = {
        'data_mprofil' : data_mprofil
    }
    return render(request, 'mprofil/v-mprofil-brg.html',context)

@login_required()    
def upmprofil(request,id_apotik):
    data_mprofil = mprofil.objects.get(id_apotik=id_apotik)
    context = {
        'data_mprofil' : data_mprofil
    }
    return render(request, 'mprofil/up-profil-brg.html',context)
   
@login_required() 
def postupmprofil(request):
    id_apotik = request.POST['id_apotik']
    nama = request.POST['nama']
    alamat = request.POST['alamat']
    gambar = request.FILES['gambar'] if 'gambar' in request.FILES else None  # Menggunakan None jika gambar tidak ada
    fecebook = request.POST['facebook']
    instagram = request.POST['instagram']
    email = request.POST['email']
    whatsapp = request.POST['whatsapp']
    
    data_mprofil = mprofil.objects.get(id_apotik=id_apotik)
    
    data_mprofil.id_apotik = id_apotik
    data_mprofil.nama = nama
    data_mprofil.alamat = alamat
    if gambar:  # Hanya mengatur gambar jika ada
        data_mprofil.gambar = gambar
    data_mprofil.facebook = fecebook
    data_mprofil.instagram = instagram
    data_mprofil.email = email
    data_mprofil.whatsapp = whatsapp
    
    data_mprofil.save()
    messages.success(request,'BERHASIL UPDATE')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def addmbrgsat(request):
    data_mbarang = mbarang.objects.all()
    context = {
        'data_mbarang' : data_mbarang
    }
    return render(request, 'mbrgsat/add-mbrgsat-brg.html', context)
    