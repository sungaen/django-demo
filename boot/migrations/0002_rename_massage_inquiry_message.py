# Generated by Django 4.0.4 on 2022-04-25 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquiry',
            old_name='massage',
            new_name='message',
        ),
    ]
