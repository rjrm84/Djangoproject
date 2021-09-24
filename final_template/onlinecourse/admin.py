from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice


# Register Inline classes
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Question and Choice models
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('lesson_title', 'question_text')

    # Added to display title in admin
    def lesson_title(self, obj):
        return obj.lesson.title


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('choice_text', 'question_id')
    list_filter = ['title']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)