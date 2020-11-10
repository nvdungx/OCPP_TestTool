from django.db import models

# Create your models here.

class UserType:
  # default field added by django
  id = models.AutoField(primary_key=True)
  # name of user
  name = models.CharField(null=False, blank=False, max_length=150)
  # email of user
  email = models.EmailField(null=False, blank=False)
  # team which user belong to
  team = models.CharField(max_length=10, blank=False, null=False)
  # user name
  # password