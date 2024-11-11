from django.db import models
from django.contrib.auth.models import User




class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    numbers = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} reserved{self.table} at {self.reservation_time}'