# Generated by Django 3.2.9 on 2021-12-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=400, null=True, verbose_name='caption'),
        ),
    ]
