from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Library Mawut',
        'subheading': 'pinjam dan baca buku disini'
    }
    return render(request, 'index.html', context)