from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.author.id