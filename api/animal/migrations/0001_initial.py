# Generated by Django 3.2 on 2022-11-11 09:27

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
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(max_length=32, verbose_name='종류')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='생일')),
                ('weight', models.CharField(max_length=10, verbose_name='몸무게')),
                ('kind', models.CharField(max_length=32, verbose_name='품종')),
                ('hospital', models.TextField(verbose_name='내원 병원')),
                ('interested_disease', models.CharField(max_length=128, verbose_name='관심 질병')),
                ('has_alergy', models.CharField(max_length=1024, verbose_name='알러지 유무')),
                ('neuter_choices', models.CharField(choices=[('IS', '유'), ('NT', '무'), ('DO', '모름')], default='IS', max_length=2, verbose_name='중성화 여부')),
                ('sex_choices', models.CharField(choices=[('MA', '남자'), ('FE', '여자')], default='MA', max_length=2, verbose_name='성별')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '반려동물 정보',
                'verbose_name_plural': '반려동물 정보',
            },
        ),
    ]
