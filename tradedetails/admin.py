from django.contrib import admin
from django.utils.html import format_html
from .models import TradeDetails

@admin.register(TradeDetails)
class TradeDetailsAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = (
        'user', 
        'traders_idea_name',
        'currency_pair', 
        'trade_signal', 
        'is_active', 
        'created_at', 
        'idea_candle_image', 
        'idea_candle_two_image', 
        'daily_candle_image', 
        'four_hour_candle',
        'line_graph_candle_image', 
        'signal_candle_image',
        'hour_candle_image', 
        'two_hour_candle_image', 
        'entry_candle_image', 
        'breakeven_candle_image',
        'take_profit_one_candle_image', 
        'take_profit_two_candle_image'
    )
    
    # Filters for quick search options
    list_filter = ('traders_idea_name', 'trade_signal', 'is_active', 'created_at')
    
    # Search fields to look up users and currency pairs
    search_fields = ('user__username', 'currency_pair')
    
    # Making the created_at field read-only
    readonly_fields = ('created_at',)
    
    # Grouping fields into collapsible sections in the admin form
    fieldsets = (
        (None, {
            'fields': ('user', 'traders_idea_name', 'currency_pair',  'trade_signal', 'is_active', 'created_at')
        }),
        ('Hour and Custom Candles', {
            'fields': (
                'idea_candle',
                'idea_candle_two',
                'daily_candle',
                'youtube_candle',
                'four_hour_candle',
                'line_graph_candle',
                'signal_candle',
                'hour_candle',
                'two_hour_candle',
                'entry_candle',
                'breakeven_candle',
                'stoploss_candle',
            ),
        }),
        ('Take Profit Candles', {
            'fields': ('take_profit_one_candle', 'take_profit_two_candle'),
        }),
    )

    # Thumbnail functions for each image field
    def idea_candle_image(self, obj):
        if obj.idea_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.idea_candle.url)
        return None
    idea_candle_image.short_description = 'Idea Candle'
    
    def idea_candle_two_image(self, obj):
        if obj.idea_candle_two:
            return format_html('<img src="{}" width="50" height="50" />', obj.idea_candle_two.url)
        return None
    idea_candle_two_image.short_description = 'Idea Candle Two'

    def youtube_candle_image(self, obj):
        if obj.youtube_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.youtube_candle.url)
        return None
    youtube_candle_image.short_description = 'Youtube Candle'

    def daily_candle_image(self, obj):
        if obj.daily_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.daily_candle.url)
        return None
    daily_candle_image.short_description = 'Daily Candle'

    def four_hour_candle_image(self, obj):
        if obj.daily_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.daily_candle.url)
        return None
    four_hour_candle_image.short_description = 'Daily Candle'

    def line_graph_candle_image(self, obj):
        if obj.line_graph_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.line_graph_candle.url)
        return None
    line_graph_candle_image.short_description = 'Line Graph Candle'

    def signal_candle_image(self, obj):
        if obj.signal_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.signal_candle.url)
        return None
    signal_candle_image.short_description = 'Signal Candle'

    def hour_candle_image(self, obj):
        if obj.hour_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.hour_candle.url)
        return None
    hour_candle_image.short_description = 'Hour Candle'

    def two_hour_candle_image(self, obj):
        if obj.two_hour_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.two_hour_candle.url)
        return None
    two_hour_candle_image.short_description = 'Two Hour Candle'

    def entry_candle_image(self, obj):
        if obj.entry_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.entry_candle.url)
        return None
    entry_candle_image.short_description = 'Entry Candle'

    def breakeven_candle_image(self, obj):
        if obj.breakeven_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.breakeven_candle.url)
        return None
    breakeven_candle_image.short_description = 'Breakeven Candle'

    def take_profit_one_candle_image(self, obj):
        if obj.take_profit_one_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.take_profit_one_candle.url)
        return None
    take_profit_one_candle_image.short_description = 'Take Profit One Candle'

    def take_profit_two_candle_image(self, obj):
        if obj.take_profit_two_candle:
            return format_html('<img src="{}" width="50" height="50" />', obj.take_profit_two_candle.url)
        return None
    take_profit_two_candle_image.short_description = 'Take Profit Two Candle'

    def stoploss_image(self, obj):
        if obj.stoploss:
            return format_html('<img src="{}" width="50" height="50" />', obj.stoploss.url)
        return None
    stoploss_image.short_description = 'Take Profit Two Candle'
