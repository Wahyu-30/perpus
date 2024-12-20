from django.db import models

# Create your models here.
class writter(models.Model):
    kode_penul = models.CharField(max_length=4)
    nama_penul = models.CharField(max_length=100)
    alamat_penul = models.CharField(max_length=50)
    kota_penul = models.CharField(max_length=40)
    kontak_penul = models.CharField(max_length=12)
    email_penul = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_penul