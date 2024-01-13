from django.template.defaulttags import url
from django.urls import include, path
from users_app.views import ActivateUser, password_reset_view

urlpatterns = [
    path('auth/users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('auth/password/reset/confirm/<uid>/<token>', password_reset_view, name='password_reset'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
