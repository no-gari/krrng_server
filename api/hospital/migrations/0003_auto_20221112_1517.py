# Generated by Django 3.2 on 2022-11-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_hospital_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalreview',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='hospitalreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hospitalreviewimage',
            name='hospital_review',
        ),
    ]
