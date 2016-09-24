from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from voting_poll.models import Question

# Create your views here.

class VotingView(TemplateView):
	template_name = "voting.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)
		context["Question"] = get_object_or_404(Question, slug=kwargs.get('slug', ''))

		return self.render_to_response(context)