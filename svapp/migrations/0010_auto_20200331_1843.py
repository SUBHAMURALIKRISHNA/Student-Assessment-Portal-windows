# Generated by Django 2.2.10 on 2020-03-31 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svapp', '0009_auto_20200331_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
