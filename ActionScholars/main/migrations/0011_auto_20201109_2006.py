# Generated by Django 3.1.1 on 2020-11-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201109_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='active_hour',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='receptive_hour',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='required_hour',
            field=models.FloatField(null=True),
        ),
    ]