from django.contrib import admin
from voting_poll.models import Question, Answer


class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	inlines = (
		AnswerInline,
	)

	prepopulated_fields = {"slug":("question",)}

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)