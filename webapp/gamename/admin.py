from django.contrib import admin
from .models import Gametitle

class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title', 'content']

admin.site.register(Gametitle, GameAdmin)
