# Generated by Django 3.2.4 on 2021-06-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, height_field='300', upload_to='posters/', width_field='200'),
        ),
    ]
