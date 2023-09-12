from django.urls import path

from.views import index,delmjenis,postupmjenis,upmjenis,vmjenis,postaddmjenis,addmjenis,postup,up,v,tambahmkelompok,tambahkelompokpost,mastermkelompok,postadd,updatmkelompok,postupdatemkelompok,deletemkelompok,index2,dashboard,add


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
    path('delmjenis/<str:kode_jenis>',delmjenis ,name='delmjenis')
]
