# Generated by Django 3.0.7 on 2020-08-18 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20200818_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scanresulttask',
            old_name='rusult_type',
            new_name='result_type',
        ),
    ]