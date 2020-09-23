from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def get_photo_path(instance, filename):
    return os.path.join('../photos', str(instance.id), filename)


# Create your models here.
class Articles(models.Model):
    article_author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    article_header = models.CharField(max_length=30)
    article_text = models.TextField(default='here comes text')
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_header

class Comments(models.Model):
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True)
    comment_article = models.ForeignKey(Articles, on_delete=models.CASCADE, blank=True)
    comment_text = models.TextField(default="comment on article...")
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=get_photo_path, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender= User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()