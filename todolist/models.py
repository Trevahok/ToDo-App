from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str (self.completed)

def create_list(sender,**kwargs):
    if kwargs['created']:
        user_list =List.objects.create(user=kwargs['instance'])
post_save.connect(create_list,sender=User)