from django.urls import path
from.views import index,tambahmkelompok,tambahkelompokpost, index2

urlpatterns = [
    path('index', index, name='index'),
    path('tambahmkelompok', tambahmkelompok, name='tambahmkelompok'),
    path('posttambahmkelompok', tambahkelompokpost, name='posttambahmkelompok'),
    path('index2', index2, name='index2')
]
