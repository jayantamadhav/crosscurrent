# Generated by Django 2.2.8 on 2019-12-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20191208_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalfee',
            name='kes',
        ),
    ]
