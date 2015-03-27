from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TEDxPBSC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','registration.views.login_user',name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/?','registration.views.register',name='register'),
    url(r'^lunch/?','registration.views.lunch',name='lunch'),
    url(r'^logout/?','registration.views.logout_user',name='logout'),
    url(r'^csv_import/?','registration.views.csv_import',name='csv_import'),
)
