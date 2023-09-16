from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Event, Category, Tag


class CategoryInline(admin.TabularInline):
    """Tabular Inline View for Category"""
    model = Category
    extra = 1


class TagInline(admin.TabularInline):
    """Tabular Inline View for Tag"""
    model = Tag
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin View for Event"""
    list_display = ['event_title_link', 'description', 'category', 'registered_tickets_count']
    list_filter = ['category']
    search_fields = ['title', 'description']
    inlines = [CategoryInline, TagInline]

    def registered_tickets_count(self, obj):
        return obj.ticket_set.count()
    
    registered_tickets_count.short_description = 'Registered Tickets'

    def event_title_link(self, obj):
        url = reverse('admin:core_ticket_changelist')  # Replace 'yourapp' with your app's name
        url += f'?event__id__exact={obj.id}'  # Add a query string to filter tickets by event
        return format_html('<a href="{}">{}</a>', url, obj.title)

    event_title_link.short_description = 'Event Title'


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
