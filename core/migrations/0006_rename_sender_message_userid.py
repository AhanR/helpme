# Generated by Django 4.0.5 on 2023-04-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='userId',
        ),
    ]