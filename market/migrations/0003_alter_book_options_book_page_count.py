# Generated by Django 5.0.4 on 2024-04-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(default=0),
        ),
    ]
