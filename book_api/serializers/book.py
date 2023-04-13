from rest_framework import serializers
from ..models import Book
from .publisher import PublisherSerializer
from .author import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    publisher_id = serializers.IntegerField()
    author_id = serializers.IntegerField()


    class Meta():
        model = Book
        fields = ('id', 'book_name', 'book_description', 'book_price', 'publisher_id', 'author_id')


    def get_publisher(self, instance):
        return PublisherSerializer(instance.publisher).data
    
    def get_author(self, instance):
        return AuthorSerializer(instance.publisher).data