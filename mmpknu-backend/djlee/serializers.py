#backend/post/serializers.py
from rest_framework import serializers
from .models import Post
from .models import Store
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Post


class NearStoreSerializer(serializers.HyperlinkedModelSerializer):
    IMAGE = serializers.ImageField(use_url=True)
    class Meta:
        fields = (
            'id',
            'GPSX',
            'GPSY',
            'LARG_CATE',
            'MID_CATE',
            'SMALL_CATE',
            'NAME',
            'IMAGENAME',
            'IMAGE',
        )
        model = Store    
