from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notifications


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the author of a post or comment to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for GET, HEAD, and OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling CRUD operations on Posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

     # Enable search filtering
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['title', 'content']  # Allow searching by title and content
    filterset_fields = ['author']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the logged-in user as the author


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling CRUD operations on Comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the logged-in user as the author


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    """Generate a feed showing posts from users the current user follows."""
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

def like_post(request, pk):
    """Allows users to like/unlike a post."""
    post = get_object_or_404(Post, id=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # Create a notification for the post author
        Notifications.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)

    else:
        # If the like already exists, it means the user is unliking the post
        like.delete()
        return Response({"message": "Like removed"}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_on_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment_text = request.data.get("comment")

    if not comment_text:
        return Response({"error": "Comment cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

    comment = Comment.objects.create(user=request.user, post=post, content=comment_text)

    # Notify the post author
    Notifications.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="commented on your post",
        target=post
    )

    return Response({"message": "Comment added successfully"}, status=status.HTTP_201_CREATED)