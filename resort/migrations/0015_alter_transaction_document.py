# Generated by Django 4.2.19 on 2025-03-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0014_gallery_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='transaction/'),
        ),
    ]
