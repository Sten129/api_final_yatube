from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Group, Comment, Follow
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer

PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = PERMISSION_CLASSES

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = PERMISSION_CLASSES

    def perform_create(self, serializer):
        serializer.save(slug=self.request.slug)

    def get_queryset(self):
        groups = Group.objects.all()
        return groups



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = PERMISSION_CLASSES

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comments = post.comments.all()
        return comments


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    pass
