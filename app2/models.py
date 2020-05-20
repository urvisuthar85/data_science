from django.db import models

# Create your models here.
class U(models.Model):
    Firstname = models.CharField(max_length=20)
    Password = models.CharField(max_length=10)

    class Meta:
        db_table = 'users'