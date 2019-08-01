from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.index),
    url(r'^add_show$', views.add_show),
    url(r'^display_show$', views.create_show),
    url(r'^show_info/(?P<num>\d+)$', views.show_info),
    url(r'^edit/(?P<num>\d+)$', views.update_show),
    url(r'^edit_show/(?P<num>\d+)$', views.edit_show),
    url(r'^shows/(?P<num>\d+)/destroy$', views.destroy),
]