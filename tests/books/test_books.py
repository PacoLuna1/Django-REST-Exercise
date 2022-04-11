import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
  'nombre, apellido',
  (
    ('Paulo', 'Coelho'),
    ('Haruki', 'Murakami'),
    ('Jordi', 'Rosado'),
  )
)
def test_author_name(nombre, apellido):
  author = Author.objects.create(name=nombre, last_name=apellido) # Create a author
  print('This is my authors name: ', author.name) # print author's name
  assert author.last_name == apellido # validate last name of the author
  assert Author.objects.count() == 1
  author.delete()
  assert Author.objects.count() == 0
  
# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
#   author = Author.objects.create(name='nombre', last_name='apellido') # Create a author
#   def model_count_mock():
#     return 4
  
#   monkeypatch.setattr(Author.objects.all(), 'count', model_count_mock)
#   assert Author.objects.all().count == 4
#   print('Haciendo el monkeypatch')