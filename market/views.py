import json
from django.http import JsonResponse
from .models import Book


def book_information(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        book_info = {
            'name': book.name,
            'author_name': book.author_name,
            'category': book.category,
            'price': str(book.price),
        }

        book_json = json.dumps(book_info)
        return JsonResponse({'book_info': book_json}, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found.'})


def books_information(request):
    books = Book.objects.all()
    books_info = []
    for book in books:
        book_info = {
            'name': book.name,
            'author_name': book.author_name,
            'category': book.category,
            'price': str(book.price),
        }
        books_info.append(book_info)
    books_json = json.dumps(books_info)
    return JsonResponse({'books_info': books_json}, safe=False)
