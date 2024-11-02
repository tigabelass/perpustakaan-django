from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Model untuk buku
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    copies = models.IntegerField()
    upload_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="book_images/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} ({self.user.is_staff})"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfil.objects.get_or_create(user=instance)
    else:
        instance.userprofil.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofil'):
        instance.userprofil.save()