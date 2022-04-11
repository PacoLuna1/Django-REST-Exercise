import pytest
from library.books.models import *

@pytest.mark.django_db
def test_author_name():
  author = Author.objects.create(name='Paulo', last_name='Coelho') # Create a author
  print('This is my authors name: ', author.name) # print author's name
  assert author.last_name == 'Coelho' # validate last name of the author
  assert Author.objects.count() == 1
  author.delete()
  assert Author.objects.count() == 0