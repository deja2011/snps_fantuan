from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tuan (models.Model):
    rest_name = models.CharField(max_length = 50, verbose_name ="restaurant name")
    min_num = models.IntegerField(verbose_name = "min participates")
    max_num = models.IntegerField(verbose_name = "max participates")
    current_num = models.IntegerField(default = 0)
    initiator = models.CharField(default = '', max_length= 50)
    start_time = models.CharField(max_length = 50, verbose_name = "start time")
    create_time = models.DateTimeField(default = timezone.now)


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

