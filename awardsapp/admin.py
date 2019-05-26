from django.contrib import admin
from __future__ import unicode_literals
from .models import Location,tags, Image, Project, Profile, Review

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Review, ReviewAdmin)