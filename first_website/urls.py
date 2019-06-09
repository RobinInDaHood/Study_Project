from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('frontpage.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('frontpage.urls')),
    path('about/', include('frontpage.urls')),
    path('menu/', include('menu.urls')),
    path('account/', include('accounts.urls')),
    path('signup/', include('accounts.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('cart/', include('order.urls')),
    path('register/', include('register.urls')),
    path('accounts/profile/', include('register.urls')),
    path('shop/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += staticfiles_urlpatterns()
