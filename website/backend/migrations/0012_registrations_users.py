# Generated by Django 4.0.1 on 2022-02-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_registrations_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrations',
            name='users',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
