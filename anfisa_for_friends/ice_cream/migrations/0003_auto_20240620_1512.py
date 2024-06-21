# Generated by Django 3.2.16 on 2024-06-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20240608_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'объект "Обертка"', 'verbose_name_plural': 'обертки'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='icecream',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='На главную'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинг'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='wrapper',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ice_cream', to='ice_cream.wrapper', verbose_name='Обертка'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]