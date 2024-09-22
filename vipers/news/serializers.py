from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    author = serializers.CharField(max_length=100)
    date_published = serializers.DateTimeField()
    content = serializers.CharField()
    image = serializers.ImageField()
    tags = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    views = serializers.IntegerField()
    shares = serializers.IntegerField()
    likes = serializers.IntegerField()
    comments = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.category = validated_data.get('category', instance.category)
        instance.views = validated_data.get('views', instance.views)
        instance.shares = validated_data.get('shares', instance.shares)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        # instance.created_at = validated_data.get('created_at', instance.created_at)
        # instance.updated_at = validated_data.get('updated_at', instance.updated_at)

        instance.save()
        return instance

