# Generated by Django 3.2 on 2022-11-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_alter_bestpart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalprice',
            name='price',
            field=models.IntegerField(max_length=128, verbose_name='가격'),
        ),
    ]