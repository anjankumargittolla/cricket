# Generated by Django 3.2.3 on 2021-05-17 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0003_match_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team1_overs',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team1_score',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team2_overs',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team2_score',
        ),
    ]
