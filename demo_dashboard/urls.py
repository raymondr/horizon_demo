from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import horizon


urlpatterns = patterns('',
    url(r'^$', 'demo_dashboard.views.splash', name='splash'),
    url(r'', include(horizon.urls)),
)

# Development static app and project media serving using the staticfiles app.
urlpatterns += staticfiles_urlpatterns()

# Convenience function for serving user-uploaded media during
# development. Only active if DEBUG==True and the URL prefix is a local
# path. Production media should NOT be served by Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
