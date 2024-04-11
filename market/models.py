from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Book Name')
    author_name = models.CharField(max_length=200, verbose_name='Author Name')
    page_count = models.IntegerField(default=0, verbose_name='Page Count')
    category = models.CharField(max_length=200, verbose_name='Category')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price')
    image = models.ImageField(null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

# შექმენით წიგნის მოდელი (name, page_count, category, author_name, price, image)
