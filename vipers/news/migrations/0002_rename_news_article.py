# Generated by Django 4.1.7 on 2023-04-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Article',
        ),
    ]
