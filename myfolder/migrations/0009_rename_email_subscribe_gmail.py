# Generated by Django 5.0.4 on 2024-05-15 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0008_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='email',
            new_name='gmail',
        ),
    ]
