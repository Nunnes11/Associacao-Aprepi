# Generated by Django 5.2 on 2025-05-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprepi', '0011_documents_alter_history_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
