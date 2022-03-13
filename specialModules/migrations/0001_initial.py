# Generated by Django 3.2.4 on 2022-03-08 16:55

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=100)),
                ('shortDiscription', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='moduleName')),
            ],
            options={
                'ordering': ['moduleName'],
            },
        ),
    ]