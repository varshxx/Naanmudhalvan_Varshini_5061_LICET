from django.contrib import admin
from .models import Song

# Register your models here
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'genre')
    search_fields = ('title', 'artist', 'album', 'genre')
    list_filter = ('genre',)
