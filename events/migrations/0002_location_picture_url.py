# Generated by Django 4.0.3 on 2023-05-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='picture_url',
            field=models.URLField(null=True),
        ),
    ]
