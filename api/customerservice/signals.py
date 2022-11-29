from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Notice, Notification


@receiver(post_save, sender=Notice)
def notice_post_save(sender, **kwargs):
    users = User.objects.all()
    name = kwargs['instance'].name
    content = kwargs['instance'].content
