# Generated by Django 3.1 on 2020-08-30 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlalgo_status',
            old_name='parent_endpoint',
            new_name='parent_mlalgorithm',
        ),
    ]
