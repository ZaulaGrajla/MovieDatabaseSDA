# Generated by Django 3.1.1 on 2020-09-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200912_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.IntegerField(blank=True, choices=[(0, 'children'), (1, 'teenagers'), (2, 'adult people')], null=True),
        ),
    ]
