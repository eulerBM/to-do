# Generated by Django 4.2.7 on 2023-11-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_to_do_bank_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_bank',
            name='key',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]
