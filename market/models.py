from django.db import models
from django.utils.translation import gettext as _


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Book Name'))
    author_name = models.CharField(max_length=200, verbose_name=_('Author Name'))
    page_count = models.IntegerField(default=0, verbose_name=_('Page Count'))
    category = models.CharField(max_length=200, verbose_name=_('Category'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('Image'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
