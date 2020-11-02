from django.db import models


class Staff(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    CHP_staff_number = models.CharField(max_length=7)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.CharField(max_length=50)

    def __str__(self):
        return self.username
