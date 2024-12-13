from django.shortcuts import render
from.models import publisher

def class_penerbit(request):
    penerbit = publisher.objects.all()
    context = {
        'Title' : 'Perpustakaan STMIK Pontianak',
        'Heading' : 'Daftar Buku Ilmu Komputer',
        'Penerbit' : penerbit,
    }
    return render(request,'penerbit.html', context)
