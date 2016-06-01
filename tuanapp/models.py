from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tuan (models.Model):
  rest_name = models.CharField(max_length = 50)
  min_num = models.IntegerField(default = 1)
  max_num = models.IntegerField(default = 3)
  init = models.CharField(max_length= 30)
  date = models.CharField(max_length = 10)
  crt_num = models.CharField(max_length= 30, default=0)
  progress = models.CharField(max_length= 30, default=0)


class Person (models.Model):
  user = models.OneToOneField(User, unique= True)
  created_tuan = models.ManyToManyField(Tuan)
  joined_tuan = models.ManyToManyField(Tuan, related_name='joind_id')
  email = models.EmailField(blank=False)  
  def __unicode__(self):
    return self.user.username


class Comment(models.Model):
  person = models.ForeignKey(Person, on_delete = models.CASCADE)
  tuan = models.ForeignKey(Tuan, on_delete = models.CASCADE)
  published = models.DateTimeField('date published')
  content = models.TextField()

