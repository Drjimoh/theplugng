from django.urls import path
from . import views


app_name = "theplug"

urlpatterns = [
    path('', views.sign_up, name="sign_up"),
    path('login', views.login_view, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout_view, name="logout"),
    path('create', views.add_post, name="create_post"),
    path('edit', views.edit_post, name="edit_post"),
    path('delete', views.delete_post, name="delete_post"),
    path('view', views.view_post, name="view_posts"),
    path('created', views.created_success, name="created"),

]