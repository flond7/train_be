# Generated by Django 4.0.4 on 2022-04-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]