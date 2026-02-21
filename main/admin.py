from django.contrib import admin

from .models import ContactMessage, Profile, Project, Skill, TimelineEntry


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "email")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "sort_order")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "sort_order", "created_at")
    list_filter = ("featured",)
    search_fields = ("title", "tech_stack")


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "entry_type", "organization", "start_date", "end_date", "is_current")
    list_filter = ("entry_type", "is_current")
    search_fields = ("title", "organization")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")
    search_fields = ("name", "email", "message")

    def has_add_permission(self, request):
        return False