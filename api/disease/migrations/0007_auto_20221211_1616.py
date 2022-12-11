# Generated by Django 3.2 on 2022-12-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0006_auto_20221211_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='disease',
            field=models.ManyToManyField(blank=True, null=True, to='disease.Disease', verbose_name='질병'),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name',
            field=models.CharField(help_text='","로 구분하여 증상을 등록해 주세요.', max_length=1024, verbose_name='증상명'),
        ),
    ]
