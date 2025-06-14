# Generated by Django 5.1.5 on 2025-04-15 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tradereasons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_candle', models.ImageField(blank=True, null=True, upload_to='monday_candles/')),
                ('tuesday_candle', models.ImageField(blank=True, null=True, upload_to='tuesday_candles/')),
                ('wednesday_candle', models.ImageField(blank=True, null=True, upload_to='wednesday_candles/')),
                ('thursday_candle', models.ImageField(blank=True, null=True, upload_to='thursday_candles/')),
                ('friday_candle', models.ImageField(blank=True, null=True, upload_to='friday_candles/')),
                ('saturday_candle', models.ImageField(blank=True, null=True, upload_to='saturday_candles/')),
                ('sunday_candle', models.ImageField(blank=True, null=True, upload_to='sunday_candles/')),
                ('swing_trade_candle', models.ImageField(blank=True, null=True, upload_to='swing_trade_candle/')),
                ('trade_reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candle_images', to='tradereasons.tradereasons')),
            ],
            options={
                'verbose_name': 'Candle image',
                'verbose_name_plural': 'Candle images',
            },
        ),
    ]
