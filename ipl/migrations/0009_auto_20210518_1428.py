# Generated by Django 3.2.3 on 2021-05-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0008_auto_20210518_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(),
        ),
    ]