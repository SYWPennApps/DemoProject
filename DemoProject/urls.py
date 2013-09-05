from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DemoProject.views.home', name='home'),
    # url(r'^DemoProject/', include('DemoProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'landing/$','BirthdayCalendar.views.landing'),
	url(r'post-login/$','BirthdayCalendar.views.postlogin'),
	url(r'home/(?P<user_id>\d+)/$','BirthdayCalendar.views.home'),
	url(r'wishlist/(?P<user_id>\d+)/$','BirthdayCalendar.views.get_user_wishlist')

)
