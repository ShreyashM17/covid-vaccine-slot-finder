# Generated by Django 4.0.1 on 2022-02-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_uid_registrations_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrations',
            name='Password',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
