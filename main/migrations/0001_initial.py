# Generated by Django 2.2.5 on 2022-04-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('hits', models.PositiveIntegerField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]