from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html
from .models import Event, Category, Location, Payment, Tag, Ticket


# class TagInline(admin.TabularInline):
#     """Tabular Inline View for Tag"""
#     model = Event.tags.through
#     extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Admin View for Location"""
    list_display = ['name', 'address', 'latitude', 'longitude']
    search_fields = ['name', 'address']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin View for Event"""
    list_display = ['title', 'description', 'category', 'ticket_price', 'registered_tickets_count']
    list_filter = ['category']
    search_fields = ['title', 'description']
    # inlines = [TagInline]


    @admin.display(ordering='registered_tickets_count')
    def registered_tickets_count(self, obj):
        url = reverse('admin:core_ticket_changelist')
        url += f'?event__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, obj.registered_tickets_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            registered_tickets_count=Count('ticket')
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin View for Category"""
    list_display = ['name']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin View for Tag"""
    list_display = ['name']
    search_fields = ['name']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'amount', 'payment_date']
    list_filter = ['event__title', 'user__username', 'payment_date']
    search_fields = ['event__title', 'user__username', 'payment_intent_id']
    list_per_page = 20


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """Admin View for Ticket"""
    list_display = ['ticket_number', 'event', 'user', 'purchase_date']
    list_filter = ['event']
    search_fields = ['ticket_number', 'event__title', 'user__username']

