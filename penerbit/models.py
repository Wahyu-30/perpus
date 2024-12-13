from django.db import models

# Create your models here.
class publisher(models.Model):
    kode_pen = models.CharField(max_length=4)
    nama_pen = models.CharField(max_length=100)
    alamat_pen = models.CharField(max_length=50)
    kota_pen = models.CharField(max_length=40)
    kontak_pen = models.CharField(max_length=12)
    email_pen = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_pen