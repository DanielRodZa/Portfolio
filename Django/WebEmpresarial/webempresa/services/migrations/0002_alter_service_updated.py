# Generated by Django 4.2.3 on 2023-07-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
