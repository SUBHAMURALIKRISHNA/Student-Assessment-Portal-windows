# Generated by Django 2.2.10 on 2020-04-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svapp', '0023_auto_20200421_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_comments',
            name='rollnumber',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
