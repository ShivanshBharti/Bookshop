from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Book(models.Model):
    book_name= models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    class Meta:
        db_table = 'books_book'

    

    def __str__(self):
        return self.book_name


