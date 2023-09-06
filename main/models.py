from django.db import models


# Create your models here.
class Gallery(models.Model):
    img = models.ImageField(default="p1.jpg")


class City(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
    img = models.ImageField(default="p1.jpg")

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(default="p1.jpg")
    price = models.CharField(max_length=50)
    des = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    person = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    detail = models.TextField()


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
