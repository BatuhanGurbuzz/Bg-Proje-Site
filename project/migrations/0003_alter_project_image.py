# Generated by Django 4.1.3 on 2023-05-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='defaults/default.png', upload_to='images'),
        ),
    ]
