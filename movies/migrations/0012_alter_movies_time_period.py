# Generated by Django 3.2.4 on 2021-06-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20210619_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='time_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.timeperiod'),
        ),
    ]