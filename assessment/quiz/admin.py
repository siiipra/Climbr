from django.contrib import admin
from .models import TeachingPoint, QuestionBank, Choice, TeachingPointQuestionMap

# Register your models here.
@admin.register(TeachingPoint)
class TeachingPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'subject', 'chapter', 'text')
    list_filter = ('class_name', 'subject')
    search_fields = ('chapter', 'text')

@admin.register(QuestionBank)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'blooms_level', 'question_image')
    search_fields = ('question_text',)
    list_filter = ('blooms_level',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('choice_text',)

@admin.register(TeachingPointQuestionMap)
class TeachingPointQuestionMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'teaching_point', 'question')
    search_fields = ('teaching_point__text', 'question__question_text')

