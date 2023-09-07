from django.urls import path
from.views import index,tambahmkelompok,tambahkelompokpost

urlpatterns = [
    path('index', index, name='index'),
    path('tambahmkelompok', tambahmkelompok, name='tambahmkelompok'),
    path('posttambahmkelompok', tambahkelompokpost, name='posttambahmkelompok')
]
