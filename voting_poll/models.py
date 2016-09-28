from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse

import uuid

class Question(models.Model):
	question = models.CharField(
		_("question"),
		max_length=255,
	)

	slug = models.SlugField(
		_("slug"),
		max_length=255,
	)

	class Meta(object):
		verbose_name = _("question")
		verbose_name_plural = _("questions")
			
	def __str__(self):
		return self.question



class Answer(models.Model):
	question = models.ForeignKey(
		Question,
		verbose_name=_("question"),
		on_delete=models.CASCADE,
		related_name="answers",
		related_query_name="answer",
	)

	answer = models.CharField(
		_("answer"),
		max_length = 255,
	)

	count = models.IntegerField(
		_("count"),
		default=0,
	)

	class Meta(object):
		verbose_name = _("Answer")
		verbose_name_plural = _("Answers")

	def __str__(self):
		return self.answer


class VotingPoll(models.Model):
	uuid = models.UUIDField(
		_('uuid'),
		editable=False,
		unique=True,
		default=uuid.uuid4
	)

	question = models.OneToOneField(
		Question,
		verbose_name=_('question'),
		on_delete=models.CASCADE,
		related_name="voting_poll",
		related_query_name="voting_poll",
	)

	start_date = models.DateTimeField(
		_('start date'),
	)

	end_date = models.DateTimeField(
		_('end date'),
	)

	class Meta(object):
		verbose_name = _("votign poll")
		verbose_name_plural = _("votign polls")

	def __str__(self):
		return _('Voting poll: {question:}').format(question=self.question)

	def is_active(self):
		return self.start_date <= timezone.now() <= self.end_date

	def is_outstanding(self):
		return timezone.now() <= self.start_date

	def is_over(self):
		return self.end_date <= timezone.now()
		
	def stats(self):
		stats = {
			'answers': {},
			'total_votes': 0,
		}

		for answer in self.question.answers.all():
			stats['answers'][answer] = {
				'votes': answer.count,
				'percentage': 0.0,
			}

		total_votes = sum(map(lambda x: x['votes'], stats['answers'].values()))

		if total_votes != 0:
			for answer, votes in stats['answers'].items():
				votes = votes['votes']
				stats['answers'][answer]['percentage'] = 100*float(votes)/float(total_votes)

		stats['total_votes'] = total_votes

		return stats

	def get_absolute_url(self):
		return reverse('voting_poll:detail', kwargs={'slug':str(self.question.slug)})