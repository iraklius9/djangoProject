from django.db import models
from django.utils.translation import gettext as _


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('Author Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('Category Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Book(models.Model):
    COVER_TYPES = [
        ('hardback', _('Hardback')),
        ('paperback', _('Paperback')),
        ('special', _('Special')),
    ]

    name = models.CharField(max_length=200, verbose_name=_('Book Name'))
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='name', verbose_name=_('Author_Name'))
    page_count = models.IntegerField(default=0, verbose_name=_('Page Count'))
    category = models.ManyToManyField(Category, verbose_name=_('Category'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('Image'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    cover_type = models.CharField(max_length=20, choices=COVER_TYPES, verbose_name=_('Cover Type'), default='hardback')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
