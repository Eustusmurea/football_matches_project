from django.contrib import admin
from django.urls import path, include
from matches.views import today_matches_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', today_matches_view, name='today_matches'),
]
