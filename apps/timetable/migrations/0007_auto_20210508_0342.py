# Generated by Django 2.2.9 on 2021-05-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20210504_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
