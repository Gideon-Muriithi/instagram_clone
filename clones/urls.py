from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    url(r'^$', views.home, name='home'),
    url(r'^all_images/$', views.all_images, name='all_images'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^image/(?P<image_id>\d+)', views.single_image, name='single_image'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)