from .models import Symptom
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Symptom)
def disease_post_save(sender, **kwargs):
    name = kwargs['instance'].name
    id = kwargs['instance'].id
    if ',' in name:
        instance = Symptom.objects.get(id=id)
        instance.delete()
