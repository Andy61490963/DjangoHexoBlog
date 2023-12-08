from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tag
from .models import homepost


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name']


@admin.register(homepost)
class homepost(admin.ModelAdmin):
    list_display = ('postname', 'introduction', 'writer', 'website', 'post_date',)
    filter_horizontal = ('tags',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'