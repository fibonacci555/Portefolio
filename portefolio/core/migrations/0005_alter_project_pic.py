# Generated by Django 4.1.3 on 2023-01-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_project_subname_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.ImageField(upload_to='media/uploads'),
        ),
    ]
