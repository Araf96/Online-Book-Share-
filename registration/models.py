from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name= models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    pro_pic = models.ImageField(upload_to='profilepic',blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    country = models.CharField(max_length=100, default='', blank=True)
    job = models.CharField(max_length=20, blank=True, default='')
    organization = models.CharField(max_length=100, default='', blank=True)


    def __str__(self):
        return self.user.username




    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class UserLibrary(models.Model):
    CATEGORY = (
        ('Educational', 'Educational'),
        ('Scientific', 'Scientific'),
        ('Fantasy', 'Fantasy'),
        ('Literature', 'Literature'),
        ('Detective', 'Detective'),
        ('Mystery', 'Mystery'),
        ('Horror', 'Horror'),
        ('Travel', 'Travel'),
        ('History', 'History'),
        ('Poetry', 'Poetry'),
        ('Journals', 'Journals'),
        ('Biographies', 'Biographies'),
        ('Other', 'Other'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='library')
    book_name = models.CharField(max_length=100, default='', blank=True)
    author_name = models.CharField(max_length=100, default='', blank=True)
    category = models.CharField(max_length=100,choices=CATEGORY, default='Other')
    publishing_year = models.CharField(max_length=10,default='',blank=True)
    book_image = models.ImageField(upload_to='bookpic',blank=True,null=True)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message


class Notification(models.Model):
    user = models.ForeignKey(User)
    book_info = models.ForeignKey(UserLibrary)
    to   = models.CharField(max_length=20)
    fromm = models.CharField(max_length=20)
    description = models.CharField(max_length=100,null=True)
    count = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.description
















