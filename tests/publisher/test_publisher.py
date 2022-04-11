import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country, publisherName',
  (
    (621,'Colonial Drive', 'Brenham','Texas', 'USA', 'Alias Editorial'),
    (2356, 'Angus Road', 'New York', 'New York', 'USA', 'AM Editores'),
    (1313, 'Prof. Jose San Benitez', 'Colima', 'Colima', 'Mexico', 'Amate Editorial'),
  )
)
def test_publisher_name(number, street, city, state, country, publisherName):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country)
  publisher = Publisher.objects.create(name=publisherName, location_id= location.id)
  print('Publisher name: ', publisher.name)
  print('Location id: ', publisher.location_id)
  assert publisher.name == publisherName
  assert Publisher.objects.count() == 1
  publisher.delete()
  location.delete()
  assert Publisher.objects.count() == 0
  
@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country, publisherName',
  (
    (3568,'Playa La Pesca', 'Nuevo Leon', 'Monterrey', 'Mexico', 'Caligrama Editores'),
    (128, 'Av De Las Torres', 'Distrito Federal', 'Tlalpan', 'Mexico', 'Ediciones el Naranjo'),
    (240, 'Jose Maria Carmona', 'Veracruz', 'Papantla', 'Mexico', 'Ediciones Era'),
  )
)
def test_publisher_location_id(number, street, city, state, country, publisherName):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country)
  publisher = Publisher.objects.create(name=publisherName, location_id= location.id)
  print('Location id: ', publisher.location_id)
  assert publisher.location_id == location.id
  location.delete()
  assert Location.objects.count() == 0

@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country, publisherName',
  (
    (63,'rue La Boétie', 'Paris','Île De France', 'France', 'Editorial CIDCLI'),
    (128, 'Av De Las Torres', 'Distrito Federal', 'Tlalpan', 'Mexico', 'Ediciones el Naranjo'),
    (230, 'Pueyrredon', 'San Francisco', 'Córdoba', 'Argentina', 'Editorial Lectorum'),
  )
)
def test_publisher_exist_id(number, street, city, state, country, publisherName):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country)
  publisher = Publisher.objects.create(name=publisherName, location_id= location.id)
  print('Publisher location id: ', publisher.location_id)
  assert publisher.location_id != 0
  assert type(publisher.location_id) is int
  location.delete()
  assert Location.objects.count() == 0
  
@pytest.mark.django_db
@pytest.mark.parametrize(
  'number, street, city, state, country, publisherName',
  (
    (33,'rue La Boétie', 'Paris','Île De France', 'France', 'Editorial Pax'),
    (801, 'Santa Rosa', 'Puente Alto', 'Puente Alto', 'Chile', 'Editorial Praxis'),
    (133, 'Prof. Jose San Benitez', 'Colima', 'Colima', 'Mexico', 'Editorial Santillana México'),
  )
)
def test_publisher_uppercase_name(number, street, city, state, country, publisherName):
  location = Location.objects.create(number=number, street=street, city=city, state=state, country=country)
  publisher = Publisher.objects.create(name=publisherName, location_id= location.id)
  print('Publisher name: ', publisher.name)
  assert type(publisher.name) is str
  assert (publisher.name).istitle()
  publisher.delete()
  assert Publisher.objects.count() == 0