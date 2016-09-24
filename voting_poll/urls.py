from django.conf.urls import url
from voting_poll.views import VotingView

app_name = "voting_poll"
urlpatterns = [
    url(r'^(?P<slug>.+)$', VotingView.as_view(), name="voting2"),
    url(r'^$', VotingView.as_view(), name="voting"),
]
