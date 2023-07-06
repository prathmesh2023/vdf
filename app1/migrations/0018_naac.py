# Generated by Django 3.2 on 2022-02-14 17:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_viewer_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='naac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]