from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("first name",max_length=30, blank=False)
    last_name = models.CharField("last name",max_length=30, blank=False)
    joined_date = models.DateField()

    def __str__(self):
        return self.first_name