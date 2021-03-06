# Generated by Django 3.2.1 on 2021-05-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('area', models.CharField(max_length=50)),
                ('leader', models.CharField(max_length=100)),
            ],
        ),
    ]
