from rest_framework import serializers
from .models import Book,Student

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Book
        fields= '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields='__all__'