from django.contrib import admin

from market.models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'page_count', 'image')
    search_fields = ('name', 'author_name')
    list_filter = ('category',)


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
