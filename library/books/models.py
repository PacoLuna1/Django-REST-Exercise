from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128, null=True)

class Location(models.Model):
  number = models.SmallIntegerField()
  street = models.CharField(max_length=128)
  city = models.CharField(max_length=128)
  state = models.CharField(max_length=128)
  country = models.CharField(max_length=128)

class Publisher(models.Model):
  name = models.CharField(max_length=128)
  location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

class Genre(models.Model):
  name = models.CharField(max_length=128, default='Desconocido')

class Book(models.Model):
  name= models.CharField(max_length = 256)
  publish_year = models.SmallIntegerField()
  pages = models.SmallIntegerField()
  price = models.DecimalField(max_digits = 6, decimal_places = 2)
  created_at = models.DateTimeField(auto_now_add=True, null= True)
  updated_at = models.DateTimeField(auto_now=True, null=True)
  authors = models.ManyToManyField(Author, through='BooksAuthors')
  genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True)
  publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, null=True)

# class BookAuthor(models.Model):
class BooksAuthors(models.Model):
	book = models.ForeignKey(Book, related_name='BookWithAuthors', on_delete=models.DO_NOTHING)
	author = models.ForeignKey(Author, related_name='AuthorWithBooks', on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id}'