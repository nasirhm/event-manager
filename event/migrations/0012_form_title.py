# Generated by Django 2.0.8 on 2018-09-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20180901_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='title',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]