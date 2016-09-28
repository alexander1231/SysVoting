from django.contrib import admin

from voting_poll.models import Answer
from voting_poll.models import Question
from voting_poll.models import VotingPoll


class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 0


class AnswerAdmin(admin.ModelAdmin):
	list_display = [
		'answer',
		'count',
	]


class QuestionAdmin(admin.ModelAdmin):
	inlines = (
		AnswerInline,
	)

	prepopulated_fields = {"slug":("question",)}


class VotingPollAdmin(admin.ModelAdmin):
	list_display = [
		'question',
		'start_date',
		'end_date',
	]


admin.site.register(VotingPoll, VotingPollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)