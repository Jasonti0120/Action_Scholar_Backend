# Generated by Django 3.1.1 on 2020-11-29 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_auto_20201110_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor_faculty',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='monitor_faculty',
            name='monitor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.AlterField(
            model_name='event_student',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='Monitor',
        ),
        migrations.DeleteModel(
            name='Monitor_Faculty',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
