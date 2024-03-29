# Generated by Django 4.1.2 on 2022-11-27 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesCategory',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default=None, null=True)),
                ('external_id', models.CharField(default=None, max_length=256, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(data_name)s', to='series_category.seriescategory')),
            ],
            options={
                'verbose_name': 'series category',
                'verbose_name_plural': 'series categories',
                'db_table': 'data_collection_series_category',
                'ordering': ['external_id'],
                'abstract': False,
            },
        ),
    ]
