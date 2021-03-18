from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Car(models.Model):
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        make_model = self.make + " " + self.model
        return make_model