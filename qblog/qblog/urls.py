# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# urlpatterns = patterns('',
#     # url(r'^admin/', include(admin.site.urls)),
#     url(r'^admin/', include(admin.site.urls)),    
#     url(r'^markdown/', include("django_markdown.urls")),
#     url(r'^', include('blog.urls')),
# )

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),    
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('blog.urls')),
)