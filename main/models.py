from django.db import models
from django.urls import reverse

# Create your models here.

class Categorys(models.Model):
    name = models.CharField(max_length=50, verbose_name="categorya kiriting: ")
    slug = models.SlugField(max_length=50, verbose_name="slug uchun")

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


    def __str__(self):
        return self.name



class CarAbout(models.Model):
    name = models.CharField(max_length=50)
    model = models.ForeignKey(to=Categorys, on_delete=models.CASCADE, verbose_name="categorya tanlang", null=True, blank=True)
    color = models.CharField(max_length=20)
    rasm = models.ImageField(upload_to="cars/", null=True, blank=True)
    speed = models.CharField(max_length=25)


    def __str__(self):
        return self.name