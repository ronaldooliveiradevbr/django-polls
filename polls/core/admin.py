from django.contrib import admin

from polls.core.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    extra = 0
    fields = ('text',)
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('text',)
    inlines = (ChoiceInline,)
