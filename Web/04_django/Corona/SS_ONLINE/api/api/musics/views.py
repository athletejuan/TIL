from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtistSerializer, ArtistDetailSerializer, MusicSerializer, MusicDetailSerializer, CommentSerializer
from .models import Artist, Music, Comment

@api_view(['GET'])
def artists(request):
    artists = Artist.objects.all()
    serializers = ArtistSerializer(artists, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    serializers = ArtistDetailSerializer(artist)
    return Response(serializers.data)

@api_view(['GET'])
def musics(request):
    musics = Music.objects.all()
    serializers = MusicSerializer(musics, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    serializers = MusicDetailSerializer(music)
    return Response(serializers.data)

@api_view(['POST'])
def music_comments(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    serializers = CommentSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(music=music)
        return Response(serializers.data)
        
@api_view(['PUT','DELETE'])
def comment_edit(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # serializers = CommentSerializer(comment)
    if request.method == "PUT":
        serializers = CommentSerializer(comment, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return HttpResponse("성공적으로 수정 되었습니다.")
    else:
        comment.delete()
        return HttpResponse("성공적으로 삭제 되었습니다.")
        


# class ArtistViewSet(viewsets.ModelViewSet):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# class ArtistDetailViewSet(viewsets.ModelViewSet):
#     queryset = Artist.music_set.all()
#     serializer_class = ArtistDetailSerializer

# class MusicViewSet(viewsets.ModelViewSet):
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer

# class MusicDetailSerializer(viewsets.ModelViewSet):
#     queryset = Music.comment_set.all()
#     serializer_class = MusicDetailSerializer

# class CommentSerializer(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
