# Generated by Django 2.2.6 on 2019-11-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalIndexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Indexer Name')),
                ('index_picture', models.ImageField(blank=True, null=True, upload_to='indexer Logo')),
                ('index_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='Indexer URL(including http/https)')),
            ],
        ),
    ]
