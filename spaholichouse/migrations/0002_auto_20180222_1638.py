# Generated by Django 2.0.2 on 2018-02-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaholichouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.CharField(max_length=100),
        ),
    ]
