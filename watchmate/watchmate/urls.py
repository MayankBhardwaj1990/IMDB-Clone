from django.contrib import admin
from django.urls import path,include
from watchlist_app.api import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/',include(urls))
]
