from django.db import models

# Create your models here.


class CarAbout(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    rasm = models.ImageField(upload_to="cars/", null=True, blank=True)
    speed = models.CharField(max_length=25)


    def __str__(self):
        return self.name