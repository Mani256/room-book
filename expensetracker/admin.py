from django.contrib import admin
from expensetracker.models import ExpenseRecord, Category

# Register your models here.
admin.site.register(ExpenseRecord)
admin.site.register(Category)