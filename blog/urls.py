from django.contrib import admin
from django.urls import path
from post.views import homepage_view
from post.views import about

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', homepage_view),
    path('about/', about)
]
