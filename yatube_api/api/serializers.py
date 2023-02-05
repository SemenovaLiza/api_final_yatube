from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, User, Follow


class UserSerializer(serializers.ModelSerializer):
    """Serializes the fields of the User model."""

    class Meta:
        fields = ('id', 'username')
        model = User


class GroupSerializer(serializers.ModelSerializer):
    """Serializes the fields of the Group model."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """Serializes the fields of the Post model."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Serializes the fields of the Comment model."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Serializes the fields of the Follow model."""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'You can not follow yourself.')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow

        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
