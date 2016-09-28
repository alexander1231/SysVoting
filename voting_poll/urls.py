from django.conf.urls import url
from django.http import HttpResponse
from voting_poll.views import HomeView
from voting_poll.views import DetailView

app_name = "voting_poll"
urlpatterns = [
    url(r'^(?P<slug>.+)$', DetailView.as_view(), name="detail"),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^/holi/',HomeView.as_view(), name="post"),
]
