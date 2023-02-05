from rest_framework import viewsets, mixins, permissions, filters
from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, UserSerializer, FollowSerializer)

from posts.models import Comment, Group, Post, User, Follow


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Implementation of CRUD methods for the User model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Implementation of CRUD methods for the Group model."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Implementation of CRUD methods for the Post model."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Implementation of CRUD methods for the Comment model."""

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = self.kwargs.get('post_id')
        queryset = Comment.objects.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('post_id'),
            author=self.request.user
        )


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Implementation of CRUD methods for the Follow model."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        queryset = Follow.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
