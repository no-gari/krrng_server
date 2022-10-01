# Generated by Django 3.1.4 on 2021-10-07 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=32, verbose_name='이름')),
                ('big_address', models.CharField(max_length=2048, verbose_name='')),
                ('small_address', models.CharField(blank=True, max_length=2048, null=True)),
                ('postal_code', models.CharField(max_length=32, verbose_name='우편 번호')),
                ('phone_number', models.CharField(max_length=32, verbose_name='휴대폰')),
                ('is_default', models.BooleanField(default=False, verbose_name='기본 배송지 설정')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
        ),
    ]
