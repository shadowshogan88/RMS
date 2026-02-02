from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html

from RecipeApp.models import AuthUserModel, CategoryModels, ContactMessage, Recipe


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'status',
        'is_read',
        'created_at',
        'read_toggle',
        'status_advance',
    )
    list_editable = ('status',)
    list_filter = ('status', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:message_id>/toggle-read/',
                self.admin_site.admin_view(self.toggle_read),
                name='contactmessage_toggle_read',
            ),
            path(
                '<int:message_id>/advance-status/',
                self.admin_site.admin_view(self.advance_status),
                name='contactmessage_advance_status',
            ),
        ]
        return custom_urls + urls

    def toggle_read(self, request, message_id):
        message = self.get_object(request, message_id)
        if message:
            message.is_read = not message.is_read
            message.save(update_fields=['is_read'])
        return redirect(request.META.get('HTTP_REFERER', '..'))

    def advance_status(self, request, message_id):
        message = self.get_object(request, message_id)
        if message:
            order = [
                ContactMessage.STATUS_PENDING,
                ContactMessage.STATUS_WORKING,
                ContactMessage.STATUS_COMPLETE,
            ]
            try:
                idx = order.index(message.status)
            except ValueError:
                idx = -1
            message.status = order[(idx + 1) % len(order)]
            message.save(update_fields=['status'])
        return redirect(request.META.get('HTTP_REFERER', '..'))

    @admin.display(description='Read/Unread')
    def read_toggle(self, obj):
        label = 'Mark Unread' if obj.is_read else 'Mark Read'
        url = reverse('admin:contactmessage_toggle_read', args=[obj.pk])
        return format_html('<a class="button" href="{}">{}</a>', url, label)

    @admin.display(description='Next Status')
    def status_advance(self, obj):
        url = reverse('admin:contactmessage_advance_status', args=[obj.pk])
        return format_html('<a class="button" href="{}">Next</a>', url)


admin.site.register([AuthUserModel, CategoryModels])
admin.site.register(Recipe)
