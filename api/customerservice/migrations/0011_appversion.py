# Generated by Django 3.2 on 2022-12-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerservice', '0010_alter_notification_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.BooleanField(default=1.0, verbose_name='버전')),
            ],
            options={
                'verbose_name': '버전 정보',
                'verbose_name_plural': '버전 정보',
            },
        ),
    ]
