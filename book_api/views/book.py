from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Book

from ..serializers import BookSerializer, PublisherSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    @action(detail=True, methods=['GET'], url_path='author')
    def get_author(self, request, pk=None):
        book = self.get_object()
        if book.author == None:
            return Response("text: This book does not have an Author")
        return Response(book.author.author_name, status=200)
    
    @action(detail=True, methods=['GET'], url_path='publisher')
    def get_publisher(self, request, pk=None):
        book = self.get_object()
        if book.publisher == None:
            return Response("This Book does not have an Publisher")
        publisher = PublisherSerializer()
        return Response(publisher['publisher_name'], status=200)