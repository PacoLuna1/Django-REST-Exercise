from rest_framework import viewsets
from rest_framework import permissions
from library.books.serializers import *

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Location to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = []

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = []

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []