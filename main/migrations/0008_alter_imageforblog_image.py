# Generated by Django 4.2.1 on 2024-03-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_medias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageforblog',
            name='image',
            field=models.ImageField(upload_to='images/blog/'),
        ),
    ]