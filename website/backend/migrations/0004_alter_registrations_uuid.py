# Generated by Django 4.0.1 on 2022-02-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_registrations_uuid_alter_registrations_document_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='uuid',
            field=models.CharField(max_length=10),
        ),
    ]
