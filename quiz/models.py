from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mountain_images/')
    height = models.IntegerField(default=0)
    region = models.CharField(max_length=255, default='Unknown')
    group = models.CharField(max_length= 255, default='Unknown')

    def __str__(self):
        return self.name