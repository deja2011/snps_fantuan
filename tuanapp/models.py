from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tuan (models.Model):
  rest_name = models.CharField(max_length = 50)
  max_num = models.CharField(max_length= 30)
  init = models.CharField(max_length= 30)
  date = models.CharField(max_length = 10)
  crt_num = models.CharField(max_length= 30, default=0)
  progress = models.CharField(max_length= 30, default=0)


class Person (models.Model):
  user = models.OneToOneField(User, unique= True)
  created_tuan = models.ManyToManyField(Tuan)
  joined_tuan = models.ManyToManyField(Tuan, related_name='joind_id')
  
  def __unicode__(self):
    return self.user.username
