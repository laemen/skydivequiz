# Generated by Django 3.0.4 on 2020-04-04 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skydivequizuser',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='skydivequizuser',
            name='skydive_license',
        ),
        migrations.RemoveField(
            model_name='skydivequizuser',
            name='skydive_license_country',
        ),
    ]