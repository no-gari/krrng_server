# Generated by Django 3.2 on 2022-11-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20221112_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='recommend_number',
            field=models.FloatField(blank=True, default=36.5, help_text='숫자가 높을수록 추천 순위가 높습니다. 기본 추천 가중치는 36.5입니다.', null=True, verbose_name='애정 온도'),
        ),
    ]
