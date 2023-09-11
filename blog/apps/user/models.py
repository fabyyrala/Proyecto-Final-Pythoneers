from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    avatar = models.ImageField(upload_to='user/avatars/', default="user/default/default.jpg")
    is_collaborator = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()





