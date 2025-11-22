from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'new')
    list_filter = ('new', 'release_year')
    search_fields = ('title', 'description')
    list_editable = ('new',)
