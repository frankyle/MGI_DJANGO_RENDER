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
            name='TradingIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candle_pattern', models.CharField(blank=True, choices=[('Engulfing', 'Engulfing Candle'), ('Small Body', 'Small Candle'), ('Pinbar', 'Pin bar Candle')], max_length=20, null=True)),
                ('fibonacci_level', models.CharField(blank=True, choices=[('38.2%', '38.2%'), ('50%', '50%'), ('61.8%', '61.8%'), ('78.6%', '78.6%')], max_length=5, null=True)),
                ('session', models.CharField(blank=True, choices=[('London', 'London Session'), ('Newyork', 'New York Session')], max_length=15, null=True)),
                ('five_min_order_block', models.BooleanField(default=False)),
                ('previous_day_color_structure', models.BooleanField(default=False)),
                ('asion_kill_zone', models.BooleanField(default=False)),
                ('london_kill_zone', models.BooleanField(default=False)),
                ('newyork_kill_zone', models.BooleanField(default=False)),
                ('flip_four_hour_candle', models.BooleanField(default=False)),
                ('fifteen_min_break_of_structure', models.BooleanField(default=False)),
                ('fvg_blocks', models.BooleanField(default=False)),
                ('change_color_ut_alert', models.BooleanField(default=False)),
                ('flactial_and_alligator', models.BooleanField(default=False)),
                ('pips_stoplost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('pips_gained', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('trade_reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trading_indicators', to='tradereasons.tradereasons')),
            ],
            options={
                'verbose_name': 'Trading indicator',
                'verbose_name_plural': 'Trading indicators',
            },
        ),
    ]
