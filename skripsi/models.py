from django.db import models

class Skripsi(models.Model):
    nim = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    judul = models.TextField()
    dosen_pembimbing = models.CharField(max_length=100)
    semester = models.IntegerField(default=1)
    
    def __str__(self):
        return self.judul