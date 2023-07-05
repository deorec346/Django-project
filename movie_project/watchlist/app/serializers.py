from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only=True)    
    release_date = serializers.DateField()
    director = serializers.CharField()
    actors = serializers.CharField()