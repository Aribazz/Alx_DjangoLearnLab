from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, comment_on_post, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user-feed'),
    path('like/<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='like-post'),
    path('<int:pk>/comment/', comment_on_post, name='comment_on_post'),

]
