from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name = "theplug"

urlpatterns = [
    path('', views.PostList.as_view(), name="sign_up"),
    path('<slug:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('login', views.login_view, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout_view, name="logout"),
    path('create', views.add_post, name="create_post"),
    path('edit', views.edit_post, name="edit_post"),
    path('delete', views.delete_post, name="delete_post"),
    path('view', views.view_post, name="posts"),
    path('created', views.created_success, name="created"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)