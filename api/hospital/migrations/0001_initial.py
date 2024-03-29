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
            name='AvailableAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=64, verbose_name='진료 동물')),
            ],
            options={
                'verbose_name': '진료 동물',
                'verbose_name_plural': '진료 동물',
            },
        ),
        migrations.CreateModel(
            name='BestPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='특화 분야')),
            ],
            options={
                'verbose_name': '특화 분야',
                'verbose_name_plural': '특화 분야',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='정확한 질병명')),
            ],
            options={
                'verbose_name': '질병 명',
                'verbose_name_plural': '질병 명',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='병원명')),
                ('number', models.CharField(max_length=64, verbose_name='연락처')),
                ('intro', models.TextField(max_length=64, verbose_name='소개글')),
                ('available_time', models.CharField(max_length=512, verbose_name='영업 시간')),
                ('rest_date', models.CharField(max_length=512, verbose_name='휴무일')),
                ('is_visible', models.BooleanField(default=True, verbose_name='노출 여부')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='도로명 주소')),
                ('address_detail', models.CharField(blank=True, max_length=1024, null=True, verbose_name='상세 주소')),
                ('latitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='위도')),
                ('longitude', models.CharField(blank=True, max_length=512, null=True, verbose_name='경도')),
                ('recommend_number', models.IntegerField(blank=True, default=0, help_text='숫자가 높을수록 추천 순위가 높습니다. 기본 추천 가중치는 0입니다.', null=True, verbose_name='추천 가중치')),
                ('available_animal', models.ManyToManyField(to='hospital.AvailableAnimal', verbose_name='진료 가능 동물')),
                ('best_part', models.ManyToManyField(to='hospital.BestPart', verbose_name='특화 분야')),
            ],
            options={
                'verbose_name': '병원',
                'verbose_name_plural': '병원',
            },
        ),
        migrations.CreateModel(
            name='HospitalPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='진료 항목')),
                ('price', models.CharField(max_length=128, verbose_name='가격')),
            ],
            options={
                'verbose_name': '진료비',
                'verbose_name_plural': '진료비',
            },
        ),
        migrations.CreateModel(
            name='HospitalReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=128, verbose_name='진료 항목')),
                ('receipt', models.ImageField(upload_to='', verbose_name='영수증 사진')),
                ('review', models.TextField(verbose_name='리뷰 내용')),
                ('likes', models.IntegerField(verbose_name='좋아요 수')),
                ('rates', models.FloatField(default=5, verbose_name='리뷰 별점')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital', verbose_name='병원')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '병원 리뷰',
                'verbose_name_plural': '병원 리뷰',
            },
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='증상명')),
            ],
            options={
                'verbose_name': '증상 명',
                'verbose_name_plural': '증상 명',
            },
        ),
        migrations.CreateModel(
            name='HospitalReviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('hospital_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospitalreview', verbose_name='리뷰')),
            ],
            options={
                'verbose_name': '병원 리뷰 이미지',
                'verbose_name_plural': '병원 리뷰 이미지',
            },
        ),
        migrations.CreateModel(
            name='HospitalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital', verbose_name='병원')),
            ],
            options={
                'verbose_name': '병원 이미지',
                'verbose_name_plural': '병원 이미지',
            },
        ),
    ]
