from django.contrib import admin

from .models import Tag, Project, ProjectImage

# Admin panel customization

class ProjecImageInLine(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link",)
    inlines = [ProjecImageInLine]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# registering models
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)