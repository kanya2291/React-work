# Generated by Django 4.2.4 on 2023-08-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('collegeName', models.CharField(max_length=150)),
                ('course', models.CharField(max_length=150)),
            ],
        ),
    ]
