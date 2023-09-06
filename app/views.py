from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Kelompok
from django.contrib import messages
# Create your views here.
def index(request):
    context= {
        'name':'front'
    }
    return render(request,'index.html',context)

def tambahmkelompok(request):
    return render(request, 'tambah-kelompok-barang.html')

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