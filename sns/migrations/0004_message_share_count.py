# Generated by Django 3.0.4 on 2022-12-21 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_auto_20221221_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='share_count',
            field=models.IntegerField(default=0),
        ),
    ]
