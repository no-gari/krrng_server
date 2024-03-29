# Generated by Django 3.2 on 2022-11-12 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0003_auto_20221112_1517'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=128, verbose_name='진료 항목')),
                ('receipt', models.ImageField(upload_to='', verbose_name='영수증 사진')),
                ('review', models.TextField(verbose_name='리뷰 내용')),
                ('rates', models.FloatField(default=5, verbose_name='리뷰 별점')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital', verbose_name='병원')),
                ('like_users', models.ManyToManyField(blank=True, null=True, related_name='like_articles', to=settings.AUTH_USER_MODEL, verbose_name='좋아요한 사람들')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '병원 리뷰',
                'verbose_name_plural': '병원 리뷰',
            },
        ),
        migrations.CreateModel(
            name='HospitalReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('hospital_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.hospitalreview', verbose_name='리뷰')),
            ],
            options={
                'verbose_name': '병원 리뷰 이미지',
                'verbose_name_plural': '병원 리뷰 이미지',
            },
        ),
    ]
