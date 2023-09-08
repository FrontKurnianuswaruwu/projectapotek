from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kelompok
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
    #ngecek kalo kode kelompok sama dengan kode kelompok yang ada didalm tabel
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

    