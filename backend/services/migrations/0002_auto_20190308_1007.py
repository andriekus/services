# Generated by Django 2.1.7 on 2019-03-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='available',
            new_name='availability',
        ),
    ]
