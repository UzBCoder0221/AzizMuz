# Generated by Django 4.2.1 on 2023-06-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='dur',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
