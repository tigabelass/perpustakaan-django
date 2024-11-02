from django.shortcuts import render,redirect
from . import models
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from PIL import Image
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# Create your views here.
def user_is_confirmed(user):
    if hasattr(user, 'userprofile'):
        return  user.is_authenticated and user.userprofil.is_confirmed
    return False


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book_list")
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})

@login_required
def book_list(request):
    books = models.Book.objects.all()
    context ={
        'title':'Bookself',
        'heading': 'Welcome, Bookself',
        'subheading': 'select your book',
        'text': 'Jika anda tertarik, datanglah ke perpustakaan mawut terdekat!',
        'buttons': 'Search Book',
        'books': books
    }
    return render(request, 'bookself/booklist.html', context)

@login_required
def add_book(request):
    if request.method == "POST" and request.FILES.get('image', None):
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        copies = int(request.POST.get('copies'))
        description = request.POST.get('description')
        image = request.FILES['image' ]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        cropped_img = crop_images(fs.path(filename))
        
        
        
        book = models.Book(title=title, author=author, genre=genre, copies=copies, description=description, image=cropped_img)
        book.save()
        return redirect('book_view', book_id=book.id)

    return render(request, 'bookself/addbook.html')

@login_required
def book_view(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    context = {
        'book':book,
    }
    return render(request, 'bookself/bookview.html', context)

@login_required
def delete_book(request):
    if request.method == "POST":
        query = request.POST['query']
        books = models.Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        if books.exists():
            books.delete()
            return redirect('book_list')
        else:
            context ={
                'title':'Book not found',
                'message': 'Mohon masukan judul buku dan penulis dengan benar'
            }
            return render(request, 'bookself/errorHandler.html', context)
    else:
        return render(request, 'bookself/deletebook.html',)

@login_required
def search_book(request):
    books = models.Book.objects.all()
    if request.method == "POST":
        query = request.POST['query']
        books = models.Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        if books.exists():
            if books.count() == 1:
                return redirect('book_view', book_id=books.first().id)
            else:
                context =  {
                    'books':books,
                    'heading': 'Hasil Pencarian',
                    'subheading': 'Buku yang anda temukan',
                    'buttons': 'Go back'
                }
                return render(request, 'bookself/booklist.html', context)
        else:
            context ={
                'title':'Book not found',
                'message': 'Mohon masukan judul buku dan penulis dengan benar',
            }
            return render(request, 'bookself/errorHandler.html', context)
    else:
        return render(request, 'bookself/searchbook.html',{'books': books})
    
def crop_images(img_path):
    img = Image.open(img_path)
    
    width, height= img.size
    new_size = min(width, height)
    img_cropped = img.crop((0,0, new_size, new_size))
    
    base_filename = os.path.basename(img_path)
    new_dir = os.path.join(settings.MEDIA_ROOT, 'book_images')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    newpath_img = os.path.join(new_dir, base_filename)
    
    img_cropped.save(newpath_img)
    
    return f"book_images/{base_filename}"