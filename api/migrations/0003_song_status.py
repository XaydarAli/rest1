# Generated by Django 5.0.7 on 2024-08-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_song_num_of_listens'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='status',
            field=models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=5),
        ),
    ]
