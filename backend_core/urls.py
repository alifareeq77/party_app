from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/', include('users_app.urls')),
    path("chat/", include("chat_app.urls"))
]
