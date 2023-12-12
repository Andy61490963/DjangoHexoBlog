from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tag
from .models import homepost

from .models import archives
from .models import archives_content

from .models import repository
from .models import repository_content


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


@admin.register(archives)
class archives(admin.ModelAdmin):
    list_display = ('postname','post_date',)


@admin.register(archives_content)
class archives_content(admin.ModelAdmin):
    list_display = ('postname', 'introduction', 'writer', 'website', 'post_date', 'ownerid')
    filter_horizontal = ('tags',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'


@admin.register(repository)
class repository(admin.ModelAdmin):
    list_display = ('postname','post_date',)


@admin.register(repository_content)
class repository_content(admin.ModelAdmin):
    list_display = ('postname', 'introduction', 'writer', 'website', 'post_date', 'ownerid')