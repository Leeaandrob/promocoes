from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from core.views import HomeView, PostDetailView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^dog/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
