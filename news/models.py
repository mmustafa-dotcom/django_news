from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     city = models.CharField(max_length=100)
#     email = models.EmailField()

class User(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    city = models.CharField(max_length=200)
    email=models.EmailField()

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname