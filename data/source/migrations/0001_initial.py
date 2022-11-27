# Generated by Django 4.1.2 on 2022-11-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0002_alter_group_secrets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='%(data_name)s', to='group.group')),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
                'db_table': 'data_collection_source',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
