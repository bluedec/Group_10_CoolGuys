# Generated by Django 4.1.3 on 2022-12-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Event', verbose_name='Imagen'),
        ),
    ]
