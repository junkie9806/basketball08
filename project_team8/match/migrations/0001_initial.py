# Generated by Django 4.1.9 on 2023-06-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('match_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
