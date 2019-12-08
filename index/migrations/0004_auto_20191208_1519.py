# Generated by Django 2.2.8 on 2019-12-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_topreviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='chief_editor_desg',
            field=models.CharField(default='DESIGNATION', max_length=400, verbose_name='chief editor designation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='abbr_title',
            field=models.CharField(max_length=200, verbose_name='Abbr. Title'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='chief_editor',
            field=models.CharField(max_length=400, verbose_name='chief editor'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='journal_name',
            field=models.CharField(max_length=200, verbose_name='Journal'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='journal_url',
            field=models.CharField(max_length=100, verbose_name='Journal URL'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='language',
            field=models.CharField(blank=True, default='N/A', max_length=100, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='origin_country',
            field=models.CharField(blank=True, default='N/A', max_length=100, verbose_name='Origin'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='publisher',
            field=models.CharField(blank=True, default='N/A', max_length=100, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='issue_name',
            field=models.CharField(max_length=200, verbose_name='Issue'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='volume_name',
            field=models.CharField(max_length=200, verbose_name='Volume name'),
        ),
    ]