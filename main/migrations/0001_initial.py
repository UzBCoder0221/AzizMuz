# Generated by Django 4.2.1 on 2023-06-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Musics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('music', models.FileField(upload_to='musics/')),
                ('music_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Music',
            },
        ),
        migrations.CreateModel(
            name='SubscribeEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('upcoming_date', models.DateField()),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('song_type', models.CharField(choices=[('single', 'Single'), ('duet', 'Duet'), ('trio', 'Trio'), ('quartet', 'Quartet')], default='single', max_length=16)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True, max_length=128, null=True)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('add_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
