# Generated by Django 4.0.1 on 2022-01-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focusapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='mimetype',
            field=models.CharField(default='application/octet-stream', max_length=512),
        ),
    ]