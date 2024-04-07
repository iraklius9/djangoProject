from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'category', 'price', 'page_count', 'image')
    search_fields = ('name', 'author_name')
    list_filter = ('category',)


admin.site.register(Book, BookAdmin)
