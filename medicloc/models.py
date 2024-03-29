from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    abbrv = models.CharField(max_length=3)

    def __str__(self):
        return self.name + "; " + self.abbrv


class State(models.Model):
    name = models.CharField(max_length=25)
    capital = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class LocalGovenment(models.Model):
    name = models.CharField(max_length=25)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=125)
    location = models.ForeignKey(LocalGovenment, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return models.name
