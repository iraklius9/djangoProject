import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from market.models import Book, Author, Category
from django.shortcuts import render, get_object_or_404


# from django.utils.translation import gettext


# def initial_page(request):
#     return JsonResponse({'message': 'Welcome to the Bookstore!\n'
#                                     'To get information about a book, use the /book/<book_id> endpoint.\n'
#                                     'To get information about all books, use the /books endpoint.\n'
#                                     'To open admin page go to /admin/ with login: admin, password: admin123'})


def initial_page(request):
    return render(request, 'initial_page.html')


# def book_information(request, book_id):
#     try:
#         book = Book.objects.get(pk=book_id)
#
#         book_info = {
#             'name': book.name,
#             'author_name': book.author_name,
#             'category': book.category,
#             'price': str(book.price),
#             'description': book.description,
#         }
#
#         book_json = json.dumps(book_info)
#         return JsonResponse({'book_info': book_json}, safe=False)
#     except Book.DoesNotExist:
#         return JsonResponse({'error': 'Book not found.'})


def books_information(request):
    books = Book.objects.values_list('name', 'author_name', 'category', 'price')
    books_info = list(books)
    return JsonResponse({'books_info': books_info}, safe=False)


# def book_listing(request):
#     all_books = Book.objects.all()
#
#     paginator = Paginator(all_books, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'book_listing.html', {'page_obj': page_obj})


def book_listing(request):
    authors = Author.objects.all()
    categories = Category.objects.all()

    author_id = request.GET.get('author')
    category_id = request.GET.get('category')

    all_books = Book.objects.all()

    if author_id:
        all_books = all_books.filter(author_name__id=author_id)

    if category_id:
        all_books = all_books.filter(category__id=category_id)

    paginator = Paginator(all_books, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_listing.html',
                  {'page_obj': page_obj,
                   'authors': authors,
                   'categories': categories})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    description = book.description
    name = book.name
    author_name = book.author_name
    categories = book.category.all()
    price = book.price
    cover = book.cover_type
    return render(request, 'book_detail.html', {
        'description': description,
        'name': name,
        'author_name': author_name,
        'categories': categories,
        'price': price,
        'cover': cover
    })
