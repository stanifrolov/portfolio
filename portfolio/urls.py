from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from newsletter.views import home,education,work,sideprojects,blog, contact

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    # url(r'^education/', education, name='education'),
    # url(r'^work/', work, name='work'),
    # url(r'^sideprojects/', sideprojects, name='sideprojects'),
    url(r'^blog/$', blog, name='blog'),
    # url(r'^contact/$', contact, name='contact'),
    url(r'^blog/post1/', 'newsletter.views.post1', name='post1'),
    url(r'^blog/post2/', 'newsletter.views.post2', name='post2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

