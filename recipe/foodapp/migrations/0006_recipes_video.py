# Generated by Django 5.0.4 on 2024-06-03 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
