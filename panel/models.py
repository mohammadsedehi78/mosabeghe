from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    countrate = models.IntegerField(default=0)
    sumrate = models.IntegerField(default=0)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

    @property
    def underscore_name(self):
        return str(self.name).replace(" ", "_")

    @property
    def edit_id(self):
        return "edit_" + self.name + "_" + self.user.username

    @property
    def delete_id(self):
        return "delete_" + self.name + "_" + self.user.username
