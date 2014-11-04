from django.conf.urls import patterns, include, url
from django.contrib import admin
from Hello import views
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Hello.views.Hello', name='Hello'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('snippets.url')),

    url(r'^admin/', include(admin.site.urls)),
)
