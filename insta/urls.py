from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.index,name = 'indexpage'),
    url(r'^profile/',views.profile,name ='profile'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^viewprofile/(?P<id>\d+)',views.view_profile,name = 'viewprofile'),
    url(r'^image/$', views.add_new_image, name='upload_image'),
    url(r'^search/$', views.search_user, name='search_profile'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^follow/(\d+)$', views.follow, name='follow'),
    url(r'^unfollow/(\d+)$', views.unfollow, name='unfollow'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
