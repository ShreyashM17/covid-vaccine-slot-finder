# Generated by Django 4.0.1 on 2022-02-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_registrations_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='Uid',
            field=models.CharField(max_length=20),
        ),
    ]
