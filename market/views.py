import json
from django.http import JsonResponse, HttpResponse
from market.models import Book
from django.shortcuts import render
from django.utils.translation import gettext


# def initial_page(request):
#     return JsonResponse({'message': 'Welcome to the Bookstore!\n'
#                                     'To get information about a book, use the /book/<book_id> endpoint.\n'
#                                     'To get information about all books, use the /books endpoint.\n'
#                                     'To open admin page go to /admin/ with login: admin, password: admin123'})


def initial_page(request):
    context = {'message': gettext('Welcome to the Bookstore!\n'
                                  'To get information about a book, use the /book/<book_id> endpoint.\n'
                                  'To get information about all books, use the /books endpoint.\n'
                                  'To open admin page go to /admin/ with login: admin, password: admin123')}
    return render(request, 'initial_page.html', context)


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
    books = Book.objects.values_list('name', 'author_name', 'category', 'price')
    books_info = list(books)
    return JsonResponse({'books_info': books_info}, safe=False)
