from django.contrib import admin
from .models import Translation

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_language', 'created_at')
    search_fields = ('user__username', 'original_text', 'translated_text')
    list_filter = ('created_at', 'target_language')