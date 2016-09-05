from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^education/', 'newsletter.views.education', name='education'),
    url(r'^work/', 'newsletter.views.work', name='work'),
    url(r'^sideprojects/', 'newsletter.views.sideprojects', name='sideprojects'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    # url(r'^blog/$', 'newsletter.views.blog', name='blog'),
    # url(r'^blog/post1/', 'newsletter.views.post1', name='post1'),
    # url(r'^blog/post2/', 'newsletter.views.post2', name='post2'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

