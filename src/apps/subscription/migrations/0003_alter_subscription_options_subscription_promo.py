# Generated by Django 4.2.6 on 2024-01-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_subscriber_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'اشتراک', 'verbose_name_plural': 'اشتراک ها'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='promo',
            field=models.BooleanField(default=False, verbose_name='Promo'),
        ),
    ]
