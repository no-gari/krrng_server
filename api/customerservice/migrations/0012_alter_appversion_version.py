# Generated by Django 3.2 on 2022-12-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerservice', '0011_appversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='version',
            field=models.FloatField(default=1.0, verbose_name='버전'),
        ),
    ]
