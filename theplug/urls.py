from django.urls import path
from . import views


app_name = "theplug"

urlpatterns = [
    path('', views.sign_up, name="sign_up"),
    path('login', views.login_view, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout_view, name="logout"),
]