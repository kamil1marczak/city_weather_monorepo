# Generated by Django 3.0.2 on 2020-01-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikeys',
            name='api_key',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]