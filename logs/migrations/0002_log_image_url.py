# Generated by Django 3.0.5 on 2020-04-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='image_url',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
