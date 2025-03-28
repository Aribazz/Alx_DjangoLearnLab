from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)