# Generated by Django 4.1.7 on 2023-02-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0007_alter_position_song"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="songs",
            field=models.ManyToManyField(through="music.Position", to="music.song"),
        ),
    ]
