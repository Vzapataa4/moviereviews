from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='movie/images/')  # 👈 este es el nuevo campo

    def __str__(self):
        return self.title

