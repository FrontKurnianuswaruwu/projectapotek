from django.urls import path

# from.views import index,postupmdafsat,delmdafsat,vmdafsat,upmdafsat,addmdafsat,postaddmdafsat,postupmsatuan,delmsatuan,upmsatuan,vmsatuan,postaddmsatuan,addmsatuan,delmjenis,postupmjenis,upmjenis,vmjenis,postaddmjenis,addmjenis,postup,up,v,tambahmkelompok,tambahkelompokpost,mastermkelompok,postadd,updatmkelompok,postupdatemkelompok,deletemkelompok,index2,dashboard,add
from.views import *

urlpatterns = [
    path('index', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('tambahmkelompok', tambahmkelompok, name='tambahmkelompok'),
    path('posttambahmkelompok', tambahkelompokpost, name='posttambahmkelompok'),
    path('index2', index2, name='index2'),
    path('mastermkelompok', mastermkelompok, name='mastermkelompok'),
    path('updatmkelompok/<str:kode_kelompok>', updatmkelompok, name='updatmkelompok'),
    path('postupdatemkelompok', postupdatemkelompok, name='postupdatemkelompok'),
    path('deletemkelompok<str:kode_kelompok>', deletemkelompok, name='deletemkelompok'),

    #Table Mapotik
    path('add', add, name='add'),
    path('postadd', postadd, name='postadd'),
    path('v', v , name='v'),
    path('up/<str:id>', up, name='up',),
    path('postup', postup, name='postup'),

    #Table Mjenis
    path('addmjenis', addmjenis, name='addmjenis'),
    path('postaddmjenis', postaddmjenis, name='postaddmjenis'),
    path('vmjenis', vmjenis, name='vmjenis'),
    path('upmjenis/<str:kode_jenis>', upmjenis, name='upmjenis'),
    path('postupmjenis', postupmjenis, name='postupmjenis'),
    path('delmjenis/<str:kode_jenis>',delmjenis ,name='delmjenis'),
    
    #Table Data Satuan
    path('addmsatuan', addmsatuan, name='addmsatuan' ),
    path('postaddmsatuan', postaddmsatuan, name='postaddmsatuan'),
    path('vmsatuan', vmsatuan, name='vmsatuan'),
    path('upmsatuan/<str:kode_satuan>',upmsatuan, name='upmsatuan' ),
    path('postupmsatuan', postupmsatuan, name='postupmsatuan'),
    path('delmsatuan/<str:kode_satuan>',delmsatuan ,name='delmsatuan'),
    
    # Satuan Bertingkat
    path('addmdafsat', addmdafsat,name="addmdafsat"),
    path('postaddmdafsat', postaddmdafsat, name='postaddmdafsat'),
    path('vmdafsat', vmdafsat, name='vmdafsat'),
    path('upmdafsat/<str:kode_daftar_satuan>', upmdafsat, name='upmdafsat'),
    path('postupmdafsat', postupmdafsat, name='postupmdafsat'),
    path('delmdafsat<str:kode_daftar_satuan>', delmdafsat, name='delmdafsat'),
    
    #Admin
    path('addadmin', addadmin, name='addadmin'),
    path('postaddadmin', postaddadmin, name='postaddadmin'),
    path('login', login, name='login'),
    path('postllogin', postllogin, name='postllogin'),
    path('vadmin', vadmin, name='vadmin'),
    path('update/<str:id_admin>', update, name='update'),
    path('postupadmin', postupadmin, name='postupadmin'),

    
    path('addmbarang', addmbarang, name='addmbarang' ),
    
    path('addprofil', addprofil,name='addprofil'),
    path('postaddmprofil', postaddmprofil,name='postaddmprofil'),
    path('vmprofil', vmprofil, name='vmprofil'),

    path('upmprofil/<str:id_apotik>', upmprofil, name='upmprofil'),
    path('postupmsatuan', postupmsatuan, name='postupmsatuan')

    path('upmprofil/<str:id_apotik>', upmprofil, name='upmprofil')

    path('addmbarang', addmbarang, name='addmbarang' )


]
