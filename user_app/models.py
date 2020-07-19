from django.db import models

# Create your models here.


class User(models.Model):
  # id is implicitiy created
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_address = models.CharField(max_length=255)
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
        return "First Name: {}".format(self.first_name)