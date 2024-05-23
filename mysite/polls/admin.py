from django.contrib import admin

from .models import Choice,Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date"]
    list_filter = ["pub_date"]

admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)