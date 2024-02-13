# Generated by Django 4.2.6 on 2024-02-10 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_alter_recipematerial_raw_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipescategory',
            options={'verbose_name': 'دسته رسپی غذا', 'verbose_name_plural': 'دسته بندی\u200cهای رسپی غذا'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='factor',
            field=models.DecimalField(decimal_places=1, default=1.5, max_digits=3, verbose_name='Factor coefficient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='food_cost',
            field=models.IntegerField(default=0, verbose_name='Food cost'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='item_profit',
            field=models.IntegerField(default=0, verbose_name='Item profit'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='menu_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Menu price'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='number_sold',
            field=models.PositiveIntegerField(default=0, verbose_name='Number sold'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='price_with_factor',
            field=models.PositiveIntegerField(default=0, verbose_name='Final price with factor'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='service_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Services price'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_cost',
            field=models.BigIntegerField(default=0, verbose_name='Total cost'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_profit',
            field=models.BigIntegerField(default=0, verbose_name='Total profit'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_sales',
            field=models.BigIntegerField(default=0, verbose_name='Total sales'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='services_fee',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Services fee'),
        ),
        migrations.AlterField(
            model_name='recipematerial',
            name='prepared_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prepared_materials', to='restaurant.recipe', verbose_name='ماده آماده شده'),
        ),
    ]