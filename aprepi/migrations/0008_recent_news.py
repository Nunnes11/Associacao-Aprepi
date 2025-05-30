# Generated by Django 5.2 on 2025-05-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprepi', '0007_alter_register_users_options_register_users_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Imagem')),
                ('text', models.TextField(verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'notícia recente',
                'verbose_name_plural': 'notícias recentes',
            },
        ),
    ]
