# Generated by Django 3.0.6 on 2020-06-08 21:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_auto_20200601_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name': 'Error', 'verbose_name_plural': 'Errors'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': 'Programming language', 'verbose_name_plural': 'Programming languages'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AddField(
            model_name='error',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='error',
            name='data',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='Error details'),
        ),
        migrations.AlterField(
            model_name='error',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Error title'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Programming language'),
        ),
        migrations.AlterField(
            model_name='url',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='url',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Language', verbose_name='Programming language'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='scraping.City', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.CharField(max_length=250, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Vacancy description'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Language', verbose_name='Programming language'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Vacancy title'),
        ),
    ]
