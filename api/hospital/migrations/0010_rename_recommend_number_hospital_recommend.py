# Generated by Django 3.2 on 2022-11-20 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20221120_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='recommend_number',
            new_name='recommend',
        ),
    ]
