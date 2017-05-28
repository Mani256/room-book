from django.db import models
import users

# Create your models here.
class ExpenseRecord(models.Model):
    user = models.ForeignKey(users.models.User)
    createdt = models.DateTimeField()
    