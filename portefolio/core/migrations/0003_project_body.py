# Generated by Django 4.1.3 on 2023-01-15 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
