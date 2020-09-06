# Generated by Django 3.1.1 on 2020-09-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200906_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.CharField(blank=True, choices=[('little kid', 7), ('teen', 13), ('EU adult', 18), ('US adult', 21), ('senator', 36)], max_length=10, null=True),
        ),
    ]
