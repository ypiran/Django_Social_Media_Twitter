from django.urls import path
from .views import HomeView, NewPostView, PostDetailView,EditPostView

app_name = 'Home'
urlpatterns = [
    path('', HomeView.as_view(), name='HomeURL'),
    path('newpost/', NewPostView.as_view(), name='NewPostURL'),
    path('post/<int:post_id>/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('Edit/<int:post_id>', EditPostView.as_view(), name='EditPost'),
]