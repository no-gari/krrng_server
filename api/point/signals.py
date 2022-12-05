import requests
from .models import PointLog
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=PointLog)
def pointlog_post_save(sender, **kwargs):
    user = kwargs['instance'].user
    title = kwargs['instance'].title
    content = kwargs['instance'].reason

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
