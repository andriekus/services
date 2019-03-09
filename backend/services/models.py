from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.title
