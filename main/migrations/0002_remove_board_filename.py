# Generated by Django 2.2.5 on 2022-04-18 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='filename',
        ),
    ]