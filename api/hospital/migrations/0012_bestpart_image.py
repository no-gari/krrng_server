# Generated by Django 3.2 on 2022-11-20 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_rename_animal_availableanimal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestpart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='아이콘'),
        ),
    ]
