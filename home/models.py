# models.py
from django.db import models
from django.contrib.auth.models import User

class catg(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class comps(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="home/images", null=True, blank=True, help_text="Enter an image URL or upload an image.")
    price = models.IntegerField()
    description = models.TextField()
    in_stock = models.BooleanField()
    category = models.ForeignKey(catg, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def get_image_url(self):
        return f"/media/{self.image}"

    def __str__(self):
        return self.name




    # image = models.CharField(max_length=200, null=True, blank=True, help_text="Enter an image URL or upload an image.")
    #
    # def get_image_url(self):
    #     if self.image.startswith(('http://', 'https://')):
    #         return self.image
    #     else:
    #         return self.image.url if self.image else None
    #
    # def __str__(self):
    #     return f"{self.image} - {self.id}"
