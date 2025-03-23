from django.db import models

# Create your models here.

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    ISBN=models.CharField(max_length=120,unique=True)
    Title=models.CharField(max_length=255)
    Author=models.CharField(max_length=255)


    def __str__(self):
        return self.Title

class Student(models.Model):

    Name=models.CharField(max_length=120)
    grade=models.CharField(max_length=50)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)


    def __str__(self):
        return self.Name
