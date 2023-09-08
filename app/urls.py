from django.urls import path
<<<<<<< HEAD
from.views import index,tambahmkelompok,tambahkelompokpost
=======



from.views import index,tambahmkelompok,tambahkelompokpost,mastermkelompok,updatmkelompok,postupdatemkelompok,deletemkelompok,index2

>>>>>>> 19f40367a29647baa8745a1765225b9e03335e1c

urlpatterns = [
    path('index', index, name='index'),
    path('tambahmkelompok', tambahmkelompok, name='tambahmkelompok'),
<<<<<<< HEAD
    path('posttambahmkelompok', tambahkelompokpost, name='posttambahmkelompok')
=======
    path('posttambahmkelompok', tambahkelompokpost, name='posttambahmkelompok'),
    path('index2', index2, name='index2'),
    path('mastermkelompok', mastermkelompok, name='mastermkelompok'),
    path('updatmkelompok/<str:kode_kelompok>', updatmkelompok, name='updatmkelompok'),
    path('postupdatemkelompok', postupdatemkelompok, name='postupdatemkelompok'),
    path('deletemkelompok<str:kode_kelompok>', deletemkelompok, name='deletemkelompok')

>>>>>>> 19f40367a29647baa8745a1765225b9e03335e1c
]
