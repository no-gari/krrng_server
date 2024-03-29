# Generated by Django 3.2 on 2022-11-20 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_disease_symptom'),
        ('hospital', '0008_alter_hospitalimage_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalprice',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disease.disease', verbose_name='질병'),
        ),
        migrations.AddField(
            model_name='hospitalprice',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital', verbose_name='병원 명'),
        ),
    ]
