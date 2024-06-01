from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mountain_images/')

    def __str__(self):
        return self.name