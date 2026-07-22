from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    dateofbirth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='directors_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='movies_images/', null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
