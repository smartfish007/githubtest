from django.conf.urls import url
from note import views
urlpatterns=[
    url(r'^$',views.home_page,name='home'),
    url(r'^note/(.+)',views.first_skip,name='first_skip')
]