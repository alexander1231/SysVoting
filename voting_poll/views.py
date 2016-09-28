from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from voting_poll.models import VotingPoll


class HomeView(TemplateView):
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)
		context["Polls"] = VotingPoll.objects.all()

		return self.render_to_response(context)


class DetailView(TemplateView):
	template_name = "detail.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)
		show_stats = False
		
		poll = get_object_or_404(VotingPoll, question__slug=kwargs.get('slug', ''))
		poll_id = poll.uuid.hex
		
		if request.COOKIES.get(poll_id, None) is not None:
			show_stats = True

		context["Poll"] = poll
		context["ShowStats"] = show_stats

		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(*args, **kwargs)

		try:
			poll = get_object_or_404(VotingPoll, question__slug=kwargs.get('slug', ''))
			answer_id = int(request.POST.get('answer')[0])
			answer = poll.question.answers.get(id=answer_id)
			answer.count = answer.count + 1;
			answer.save()
		except Exception as msg:
			raise Exception(msg)

		context["Poll"] = poll
		context["Success"] = True

		response = self.render_to_response(context)
		response.set_cookie(poll.uuid.hex, 'true', max_age = 5000000000) 

		return response
