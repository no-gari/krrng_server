# Generated by Django 3.1.4 on 2021-02-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210202_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='anonymous user', max_length=32, verbose_name='닉네임'),
        ),
    ]
