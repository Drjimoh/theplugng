# Generated by Django 4.0.4 on 2022-07-14 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theplug', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
