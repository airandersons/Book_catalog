# Generated by Django 4.0.6 on 2022-07-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0003_alter_book_bookcover_alter_book_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookcover',
            field=models.ImageField(upload_to=''),
        ),
    ]
