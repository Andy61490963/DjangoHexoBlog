# Generated by Django 5.0 on 2024-01-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_alter_archives_content_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository_content',
            name='ppt_file',
            field=models.FileField(blank=True, upload_to='ppt/'),
        ),
    ]
