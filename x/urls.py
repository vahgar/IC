from django.conf.urls import include, url

urlpatterns = [
    url(r'^index/$','x.views.index',name="index"),
    url(r'^icbc/$','x.views.icbc',name="icbc"),


]