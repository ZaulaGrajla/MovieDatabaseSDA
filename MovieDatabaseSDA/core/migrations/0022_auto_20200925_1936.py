# Generated by Django 3.1.1 on 2020-09-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200912_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('title',)},
        ),
    ]
