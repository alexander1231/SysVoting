from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
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
