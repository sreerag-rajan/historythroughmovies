# Generated by Django 3.2.4 on 2021-06-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movies_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='lenght',
            field=models.CharField(help_text='Use HH:MM:SS format', max_length=10),
        ),
    ]