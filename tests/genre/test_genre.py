import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
  'name',
  (
    ('Fantasy'),
    ('Comedy'),
    ('Horror'),
  )
)
def test_genre_name(name):
  genre = Genre.objects.create(name=name) # Create a author
  print('This is my authors name: ', genre.name) # print author's name
  assert genre.name == name # validate last name of the author
  assert Genre.objects.count() == 1
  genre.delete()
  assert Genre.objects.count() == 0

@pytest.mark.django_db
@pytest.mark.parametrize(
  'name',
  (
    ('Mystery'),
    ('Romance'),
    ('Thriller'),
  )
)
def test_genre_exist(name):
  genreList = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller']
  genre = Genre.objects.create(name=name)
  print(genre.name, 'exist in', genreList)
  assert genre.name in genreList
  genre.delete()
  
@pytest.mark.django_db
@pytest.mark.parametrize(
  'name',
  (
    ('Lapiz'),
    ('Papel'),
    ('Roca'),
  )
)
def test_genre_not_genre(name):
  genreList = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller']
  genre = Genre.objects.create(name=name)
  print(genre.name, 'not exist in', genreList)
  assert genre.name not in genreList
  genre.delete()
  
@pytest.mark.django_db
@pytest.mark.parametrize(
  'name',
  (
    ('Drama'),
    ('Thriller'),
    ('Action'),
  )
)
def test_genre_type(name):
  genre = Genre.objects.create(name=name)
  print('Genre:', genre.name, 'type: ', type(genre.name))
  assert type(genre.name) is not int
  assert type(genre.name) is str
  genre.delete()