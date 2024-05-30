from django.urls import path, include
from . import views



urlpatterns = [
        path('', views.index, name='index'),
        path('signup/', views.sign_up_view, name='signup'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('about/', views.about, name='about'),
        path('faq/', views.faq, name='faq'),
        path('privacy/', views.privacy, name='privacy'),
        path('contact/', views.contact, name='contact'),
        path('transactions/', views.transaction, name='transaction'),
        path('report/', views.report, name='report'),
        path("login/", views.user_login, name='login'),
        path("accounts/", include("django.contrib.auth.urls")),
        path('accounts/profile', include('django.contrib.auth.urls'))

]
