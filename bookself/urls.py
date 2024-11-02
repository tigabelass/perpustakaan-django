from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('booklist/', views.book_list, name="book_list"),
    path('', views.index, name='home'),
    path('book-view/<int:book_id>/', views.book_view, name="book_view"),
    path('add-book/', views.add_book, name="add_book"),
    path('delete-book/', views.delete_book, name="delete_book"),
    path('search-book/', views.search_book, name="search_book"),
    path('login/', auth_views.LoginView.as_view(template_name="register/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    path('register/', views.register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
