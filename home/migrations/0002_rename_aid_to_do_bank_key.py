# Generated by Django 4.2.7 on 2023-11-28 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='to_do_bank',
            old_name='aid',
            new_name='key',
        ),
    ]
