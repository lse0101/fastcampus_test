from django.db import models

class User(models.Model):
  user_name = models.CharField(max_length=20)
  user_type = models.IntegerField()
