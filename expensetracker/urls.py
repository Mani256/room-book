from django.conf.urls import url
from expensetracker import views


urlpatterns = [
    url('^$',views.home, name='home'),
]