from django.contrib import admin
from .models import Paper, Review, FileHistory, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class FileHistoryInline(admin.StackedInline):
    model = FileHistory


class PaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'keywords', 'owner_name', 'status']
    inlines = [FileHistoryInline, ]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['paper_title', 'reviewer_name', 'nil_a', 'nil_b', 'nil_c']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Review, ReviewAdmin)