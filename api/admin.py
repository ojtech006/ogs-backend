from django.contrib import admin
from .models import ContactMessage, Product  # include Product if not already

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  # ✅ Replaced 'subject' with 'phone'
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)
