from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=128, verbose_name='정확한 질병명')

    class Meta:
        verbose_name = '질병 명'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Symptom(models.Model):
    disease = models.ManyToManyField(Disease, verbose_name='질병', null=True, blank=True)
    name = models.CharField(max_length=1024, verbose_name='증상명', help_text='","로 구분하여 증상을 등록해 주세요.')

    class Meta:
        verbose_name = '증상 명'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
