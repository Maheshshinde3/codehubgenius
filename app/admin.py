from django.contrib import admin
from .models import Question,Option






class optionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [optionInline]


admin.site.register(Question, QuestionAdmin)
