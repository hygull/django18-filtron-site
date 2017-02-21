from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'PyApp.views.home', name='home'),
    url(r"^pyapp/",include("PyApp.urls")),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
]
