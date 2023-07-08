from rest_framework import serializers
from .models import Thing ,Post
# allow me to cibert data come from database to JSON file
class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Thing
        fields = ('id', 'owner', 'name', 'desc', 'created_at', 'updated_at')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('id','title','desc')