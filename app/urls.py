from django.urls import path

from.views import index,postup,up,v,tambahmkelompok,tambahkelompokpost,mastermkelompok,postadd,updatmkelompok,postupdatemkelompok,deletemkelompok,index2,dashboard,add


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
    path('postup', postup, name='postup')
]
