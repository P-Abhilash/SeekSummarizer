# Generated by Django 2.2 on 2021-06-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Summarizer', '0004_all_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_sum',
            name='summary',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='save_sum',
            name='summary',
            field=models.CharField(max_length=5000),
        ),
    ]
