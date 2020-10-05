from django.shortcuts import get_object_or_404
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artist, Music
from .serializers import *


@api_view(['GET', 'POST'])
def artist_list_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    else:
        # serializers.py에서 import한 Serializer의 첫번째 인자를 키워드 없이 입력하면 인스턴스로 처리되어 유효성 검사를 통과하지 못한다.
        # 인스턴스 없이 데이터만을 인자로 넣고자 할때는 data 키워드와 함께 사용해야 한다.
        # 인스턴스가 들어가는 경우에는 data 키워드 없이도 사용가능하다.
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def artist_music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def artist_detail_music_create(request, artist_pk):
#     artist = get_object_or_404(Artist, pk=artist_pk)
#     if request.method == 'GET':
#         serializer = ArtistSerializer(artist)
#         return Response(serializer.data)
#     else:
#         serializer = MusicSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(artist=artist)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail_update_delete(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        music.delete()
        return Response({ 'id': music_pk }, status=status.HTTP_204_NO_CONTENT)