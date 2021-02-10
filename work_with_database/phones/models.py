from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    price = models.TextField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.id}: {self.name} {self.image}"
