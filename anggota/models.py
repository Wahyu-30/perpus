from django.db import models

class member(models.Model):
    kode_ang = models.CharField(max_length=4)
    nama_ang = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=50)
    no_phone = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    angkatan = models.CharField(max_length=4)

    def __str__(self):
        return self.nama_ang
