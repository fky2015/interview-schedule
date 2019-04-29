from rest_framework import serializers
from .models import Feed

class FeedSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ('url', 'title','link',
        'content','category','createTime')
