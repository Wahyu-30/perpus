from django.shortcuts import render
from.models import writter

def class_penulis(request):
    penulis = writter.objects.all()
    context = {
        'Title' : 'Perpustakaan STMIK Pontianak',
        'Heading' : 'Daftar Buku Ilmu Komputer',
        'Penulis' : penulis,
    }
    return render(request,'penulis.html', context)
