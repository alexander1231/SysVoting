from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class VotingPollConfig(AppConfig):
	name = 'voting_poll'
	verbose_name = _('Voting Poll')

	label = 'voting_poll'