# Generated by Django 5.1 on 2024-09-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_images/'),
        ),
    ]
