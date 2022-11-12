from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=128, verbose_name='정확한 질병명')

    class Meta:
        verbose_name = '질병 명'
        verbose_name_plural = verbose_name


class Symptoms(models.Model):
    models.ForeignKey(Disease, verbose_name='증상', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='증상명')

    class Meta:
        verbose_name = '증상 명'
        verbose_name_plural = verbose_name
