# Generated by Django 5.0.4 on 2024-05-09 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0004_lavozim_services_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='lavozim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfolder.lavozim'),
        ),
    ]
