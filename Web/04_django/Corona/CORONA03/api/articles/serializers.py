from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(
        # list 형태로 응답되기 때문에(댓글 개수 보장x) many=True 옵션 필수
        many=True,
        # read_only=True,
    )

    comment_count = serializers.IntegerField(
        # 1은 N의 개수를 보장할 수 없음
        # dotted notation을 활용할 수 있음
        source='comment_set.count',
        # read_only=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', 'comment_count',)
        # fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count',)


class ArticleListSerializer(serializers.ModelSerializer):

    # content = models.CharField(required=False)
    class Meta:
        model = Article
        fields = ('id', 'title',)

