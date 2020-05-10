from .models import Artist, Music, Comment
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class ArtistDetailSerializer(serializers.ModelSerializer):
    musics_count = serializers.IntegerField(source='musics.count')
    # musics_count = MusicSerializer(source='music_set', many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'musics_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']

class MusicDetailSerializer(serializers.ModelSerializer):
    # comments = serializers.CharField(source='comment_set.all')
    comments = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'comments']