# Generated by Django 4.2.6 on 2024-01-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_accesses'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Province'),
        ),
    ]
