# Generated by Django 4.1.9 on 2023-05-24 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='age',
        ),
    ]
