from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("news.urls",namespace="news")),
    # path('ckeditor/',include("ckeditor_uploader.urls")),
    # # path('accounts/',include('django.contrib.auth.urls')),
    # path('UserPanel/',include('accounts.urls')),
    # path("comment/",include("comment.urls")),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
]




urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)