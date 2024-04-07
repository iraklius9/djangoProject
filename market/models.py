from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    page_count = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

# შექმენით წიგნის მოდელი (name, page_count, category, author_name, price, image)
