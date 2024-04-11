from django.urls import path
from market import views

urlpatterns = [
    path('book/<int:book_id>', views.book_information, name='book_information'),
    path('books/', views.books_information, name='books_information'),
]

