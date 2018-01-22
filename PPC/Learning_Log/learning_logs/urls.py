# urls
# Created by JKChang
# 16/01/2018, 14:21
# Tag:
# Description: 

"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    # ^ -> begining, $-> end

    # # Show all topics.
    # url(r'^topics/$', views.topics, name='topics'),
    #
    # # Detail page for a single topic.
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
