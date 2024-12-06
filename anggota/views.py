from django.shortcuts import render
from.models import member

def ang(request):
    angt = member.objects.all()
    context = {
        'Title' : 'Perpustakaan STMIK Pontianak',
        'Heading' : 'Daftar Anggota Perpustakaan',
        'Anggota' : angt,
    }
    return render(request,'anggota.html', context)
