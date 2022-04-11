import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country',
  (
    (621,'Colonial Drive', 'Brenham','Texas', 'USA'),
    (2356, 'Angus Road', 'New York', 'New York', 'USA'),
    (1313, 'Prof. Jose San Benitez', 'Colima', 'Colima', 'Mexico'),
  )
)
def test_location_street(number, street, city, state, country):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country) # Create a author
  print('Street: ', location.street) # print author's name
  assert location.street == street # validate last name of the author
  assert Location.objects.count() == 1
  location.delete()
  assert Location.objects.count() == 0
  
@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country',
  (
    (3568,'Playa La Pesca', 'Nuevo Leon', 'Monterrey', 'Mexico'),
    (128, 'Av De Las Torres', 'Distrito Federal', 'Tlalpan', 'Mexico'),
    (240, 'Jose Maria Carmona', 'Veracruz', 'Papantla', 'Mexico'),
  )
)
def test_location_correct_number(number, street, city, state, country):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country) # Create a author
  print('Number: ', location.number)
  assert location.number > 0
  assert type(location.number) is int
  assert location.number == number
  location.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country',
  (
    (63,'rue La Boétie', 'Paris','Île De France', 'France'),
    (801, 'Santa Rosa', 'Puente Alto', 'Puente Alto', 'Chile'),
    (230, 'Pueyrredon', 'San Francisco', 'Córdoba', 'Argentina'),
  )
)
def test_location_state(number, street, city, state, country):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country) # Create a author
  print('State: ', location.state)
  assert type(location.state) is str
  assert (location.state).istitle()
  location.delete()