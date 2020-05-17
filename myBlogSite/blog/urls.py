from django.conf.urls import url

from myBlogSite.blog import views

url_patterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_drafts_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post(), name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment(), name='approve_comment'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment(), name='remove_comment'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post(), name='publish_post'),
]