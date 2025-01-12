# Generated by Django 4.1.7 on 2023-04-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='team_logos')),
                ('founded', models.DateField()),
                ('stadium', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=100)),
                ('captain', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='A brief description of the team and its history')),
                ('website', models.URLField()),
            ],
        ),
    ]
