from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Book

from ..serializers import BookSerializer, PublisherSerializer


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        method='get',
        operation_description="Get Book's Author",
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                title="Request Body",
                properties={
                    "Author_name": openapi.Schema(
                        title="Author name",
                        description="Name of the Author of the specified book",
                        type=openapi.TYPE_STRING
                    ),
                },
            )
        },
    ) 
    @action(detail=True, methods=['GET'], url_path='author')
    def get_author(self, request, pk=None):
        book = self.get_object()
        if book.author == None:
            return Response("text: This book does not have an Author")
        return Response(book.author.author_name, status=200)
    
    @swagger_auto_schema(
        method='get',
        operation_description="Get Book's Publisher",
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                title="Request Body",
                properties={
                    "publisher_name": openapi.Schema(
                        title="Publisher name",
                        description="Name of the Publisher of the specified book",
                        type=openapi.TYPE_STRING
                    ),
                },
            )
        },
    )
    @action(detail=True, methods=['GET'], url_path='publisher')
    def get_publisher(self, request, pk=None):
        book = self.get_object()
        if book.publisher == None:
            return Response("This Book does not have an Publisher")
        publisher = PublisherSerializer()
        return Response(publisher['publisher_name'], status=200)