from django.db import models

# Create your models here.


class CarAbout(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    speed = models.CharField(max_length=25)


    def __str__(self):
        return self.name