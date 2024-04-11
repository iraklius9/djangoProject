from django.urls import path
from market import views

app_name = 'market'

urlpatterns = [
    path('book/<int:book_id>', views.book_information, name='book_information'),
    path('books/', views.books_information, name='books_information'),
    path('book_listing/', views.book_listing, name='book_listing'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
]

