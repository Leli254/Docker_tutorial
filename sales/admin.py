from django.contrib import admin
from .models import SalesData

@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'sales', 'month', 'date', 'updated')
    search_fields = ('product_name', 'sales',  'month', 'date', 'updated')
    list_filter = ('product_name', 'sales', 'month', 'date', 'updated')
    readonly_fields = ('date', 'updated')
    ordering = ('-date', '-updated')
    fieldsets = (
        (None, {
            'fields': ('product_name', 'sales',  'month',)
        }),
        ('Date Information', {
            'fields': ('date', 'updated'),
            'classes': ('collapse',)
        })
    )