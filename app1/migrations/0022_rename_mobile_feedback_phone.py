# Generated by Django 4.0.4 on 2022-05-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='mobile',
            new_name='phone',
        ),
    ]
