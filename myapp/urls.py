from django.conf.urls import url

from myapp import views

urlpatterns=[
    url(r'^hello/',views.index,name='hello'),
    url(r'^getphone/',views.get_phone),
    url(r'^getlephone/',views.get_telephone),
    url(r'^dogetphone/',views.do_get_phone,name='do_get_pthone'),
    url(r'^genrate_response/',views.genrate_response),
    url(r'^get_error/',views.get_error),
    url(r'^get_jokes/(?P<page>\d+)/',views.jokes,name='jokes'),

]