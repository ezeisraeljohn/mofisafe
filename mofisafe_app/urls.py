from django.urls import path, include
from . import views



urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.sign_up_view, name='signup'),
        path("accounts/", include("django.contrib.auth.urls")),
        path("accounts/login/", include('django.contrib.auth.urls')),
        path('accounts/profile', include('django.contrib.auth.urls'))
]
