import requests
from django.dispatch import receiver
from asgiref.sync import sync_to_async
from django.db.models.signals import post_save
from .models import User, Notice, Notification


@receiver(post_save, sender=Notification)
def notification_post_save(sender, **kwargs):
    if kwargs['created']:
        pass
    else:
        user = kwargs['instance'].user
        title = kwargs['instance'].title
        content = kwargs['instance'].content

        url = "https://onesignal.com/api/v1/notifications"

        payload = {
            "include_external_user_ids": [
                str(user.id)
            ],
            "app_id": "c028e613-8406-43a8-ba01-fbff5754aa95",
            "headings": {
                "ko": title,
                "en": title,
            },
            "contents": {
                "ko": content,
                "en": content,
            },
            "name": "INTERNAL_CAMPAIGN_NAME"
        }
        headers = {
            "accept": "application/json",
            "Authorization": 'Basic MzM5OTk3MjAtOTNkYi00ODRlLWE2YjctNDE0MDYzN2FmYzk5',
            "Content-Type": "application/json"
        }
        requests.post(url, json=payload, headers=headers)


@receiver(post_save, sender=Notice)
def notice_post_save(sender, **kwargs):
    users = User.objects.all()
    name = kwargs['instance'].name
    content = kwargs['instance'].content
    for user in users:
        sync_to_async(save_notification(user, name, content), thread_sensitive=True)


def save_notification(user, name, content):
    notification = Notification.objects.create(
        user=user,
        sort='공지',
        title=name,
        content=content
    )
    notification.save()
