# Generated by Django 3.1.1 on 2020-11-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_faculty_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
