# Generated by Django 3.0.6 on 2021-01-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210106_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='states',
            new_name='status',
        ),
    ]