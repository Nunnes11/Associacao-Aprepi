# Generated by Django 5.2 on 2025-05-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprepi', '0013_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Imagem')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
    ]
