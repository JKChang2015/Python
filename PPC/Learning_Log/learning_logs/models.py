from django.db import models


# Create your models here.

class Topic(models.Model):
    ''''User's learning Topics'''
    text = models.CharField(max_length=200)  # max_length of the contents
    date_added = models.DateField(auto_now_add=True)  # auto-set current time

    def __str__(self):
        ''''return the text field'''
        return self.text
