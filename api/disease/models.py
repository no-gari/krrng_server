from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=128, verbose_name='증상명')

    class Meta:
        verbose_name = '증상 명'
        verbose_name_plural = verbose_name


class Disease(models.Model):
    models.ManyToManyField(Symptom, verbose_name='증상')
    name = models.CharField(max_length=128, verbose_name='정확한 질병명')

    class Meta:
        verbose_name = '질병 명'
        verbose_name_plural = verbose_name
