# Generated by Django 4.1.3 on 2022-12-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
    ]