from django.urls import path

from post.views import index_view
from .views import *

urlpatterns = [
    path('index/', index_view),
    path('create/', create_view),
    path('update/', update_view),
    path('detail/', detail_view),
    path('delete/', delete_view)


]
