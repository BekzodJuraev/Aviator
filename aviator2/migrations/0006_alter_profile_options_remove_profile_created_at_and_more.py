# Generated by Django 4.2.4 on 2023-10-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviator2', '0005_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
