from django.urls import path
from .views import *

app_name = 'Home'
urlpatterns = [
    path('', HomeView.as_view(), name='HomeURL'),
    path('newpost/', NewPostView.as_view(), name='NewPostURL'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('Edit/<int:post_id>/', EditPostView.as_view(), name='EditPost'),
    path('Delete/<int:post_id>/', DeletePostView.as_view(), name='DeletePost'),
    path('Reply/<int:post_id>/<int:comment_id>/', AddReplyPostView.as_view(), name='AddReply'),
    path('Like/<int:post_id>', LikePostView.as_view(), name='PostLike'),
    path('Reply/<int:post_id>', AddReplyPostView.as_view(), name='Follow'),
]