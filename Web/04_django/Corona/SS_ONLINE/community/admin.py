from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'rank', 'created_at', 'updated_at', ]

admin.site.register(Review, ReviewAdmin)