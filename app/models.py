

from django.db import models

class Kelompok(models.Model):
    kode_kelompok = models.CharField(max_length=4, primary_key=True)
    nama_kelompok = models.CharField(max_length=30)
    usertime = models.DateTimeField(auto_now=True)
    
