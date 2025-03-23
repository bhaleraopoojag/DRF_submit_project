from django.shortcuts import render

from rest_framework import viewsets
from .models import Book,Student
from .serializers import BookSerializer,StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset =Book.objects.all()
    serializer_class = BookSerializer

    # book/{bookid}/stud
    @action(detail=True,methods=['get'])
    def stud(self,request,pk=None):
        book=Book.objects.get(pk=pk)
        studs=Student.objects.filter(book=book)
        studs_serializer=StudentSerializer(studs,many=True,context={'request':request})
        return Response(studs_serializer.data)
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.filter()
    serializer_class = StudentSerializer

    #stud/{studid}/book
    # @action(detail=True,methods=['get'])
    # def bookie(self,request,pk=None):
    #     stud=Student.objects.get(pk=pk)
    #     books=Book.objects.filter(stud=stud)
    #     books_serializer=BookSerializer(books,many=True,context={'request':request})
    #     return Response(books_serializer.data)




