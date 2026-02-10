from django.contrib import admin
from .models import ChatMessage, BankStatement


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_preview', 'created_at']
    list_filter = ['created_at']
    
    def message_preview(self, obj):
        return obj.message[:50]


@admin.register(BankStatement)
class BankStatementAdmin(admin.ModelAdmin):
    list_display = ['user', 'file_name', 'uploaded_at']
    list_filter = ['uploaded_at']
