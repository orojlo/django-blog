from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage_view
from aboutpage.views import about

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', homepage_view),
    path('about/', about),
    path('post/', include('post.urls'))
]
