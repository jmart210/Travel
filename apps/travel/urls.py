from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login$', views.log_register, name="login"),
    url(r'^register$', views.log_register, name="register"),
    url(r'^landing$', views.landing, name="landing"),
    url(r'^add$', views.add, name="add"),
    url(r'^destination$', views.destination, name="destination"),
    url(r'^logout$', views.logout, name="logout"),
]
