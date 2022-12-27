from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class carsdata(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)

    class Meta:
        db_table = "cars"
