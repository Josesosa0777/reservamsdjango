# Generated by Django 4.0.3 on 2022-05-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplelist',
            name='admin_status',
            field=models.BooleanField(default=False),
        ),
    ]
