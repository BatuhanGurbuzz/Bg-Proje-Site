# Generated by Django 4.1.3 on 2023-05-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Sertifika formu Ayarları',
                'verbose_name_plural': 'Sertifika Formu',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Sosyal medya formu Ayarları',
                'verbose_name_plural': 'Sertifika Formu',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'İletişim formu Ayarları', 'verbose_name_plural': 'İletişim Formları'},
        ),
        migrations.CreateModel(
            name='Personalİnfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('school', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('lang_categories', models.ManyToManyField(to='pages.category')),
            ],
            options={
                'verbose_name': 'Kişisel Bilgiler formu Ayarları',
                'verbose_name_plural': 'Kişisel Bilgiler Formu',
            },
        ),
    ]