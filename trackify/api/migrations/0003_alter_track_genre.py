# Generated by Django 4.0 on 2021-12-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_track_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.CharField(max_length=24),
        ),
    ]
