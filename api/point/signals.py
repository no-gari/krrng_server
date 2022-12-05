from .models import PointLog
from api.customerservice.models import Notification
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=PointLog)
def pointlog_post_save(sender, **kwargs):
    user = kwargs['instance'].user
    title = kwargs['instance'].title
    content = kwargs['instance'].reason
    point = kwargs['instance'].amount

    noti = Notification.objects.create(
        sort='적립' if point >= 0 else '차감',
        user=user,
        title=title,
        content=content
    )
    noti.save()
