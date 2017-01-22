from django.conf.urls import url
from cooking_app import views
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
]