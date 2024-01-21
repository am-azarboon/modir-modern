# Generated by Django 4.2.6 on 2024-01-21 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
                ('type', models.CharField(choices=[('MOBILE_VERIFICATION_CODE', 'کد تاییدیه موبایل')], max_length=128, verbose_name='نوع اعلان')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان اعلان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح اعلان')),
                ('image', models.ImageField(blank=True, max_length=512, null=True, upload_to='images/notifications/')),
                ('kwargs', models.JSONField(blank=True, null=True, verbose_name='آرگومان\u200c\u200cهای کلیدی')),
                ('send_notify', models.BooleanField(default=True, verbose_name='ارسال اعلان')),
                ('is_showing', models.BooleanField(default=True, verbose_name='نمایش دادن')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='به کاربر')),
            ],
            options={
                'verbose_name': 'اعلان',
                'verbose_name_plural': 'اعلان ها',
                'ordering': ('-id',),
            },
        ),
    ]
