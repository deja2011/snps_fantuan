from django.db import models

# Create your models here.
class Tuan (models.Model):
  rest_name = models.CharField(max_length = 50)
  max_num = models.CharField(max_length= 30)
  init = models.CharField(max_length= 30)
  date = models.CharField(max_length = 10)
  crt_num = models.CharField(max_length= 30, default=0)
  progress = models.CharField(max_length= 30, default=0)
