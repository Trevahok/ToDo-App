from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    ''' A model for user profile page that stores all the specifics. '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be a valid number. ")

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    desc=models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ph_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    last_activity_ip = models.GenericIPAddressField(default = '0.0.0.0')
    dp=models.ImageField(upload_to ='userdps/',default='defautl.png' ,blank=True,null=True)
    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile =UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


