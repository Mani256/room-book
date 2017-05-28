from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=40, primary_key=True)
    createdby = models.CharField(max_length=40)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name= "Category of the expense record"


class ExpenseRecord(models.Model):
    user = models.ForeignKey('users.User')
    transaction_date = models.DateTimeField()
    category = models.ForeignKey(Category)
    is_room_expense = models.BooleanField()
    amount = models.FloatField()
    balance = models.FloatField()

    def __str__(self):
        return self.user.__str__() +" on " + str(self.transaction_date) +": "+ str(self.amount)

    class Meta:
        verbose_name= "Transaction record for the user"


