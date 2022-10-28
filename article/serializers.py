from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        

        
# 방법 1        
# class ArticleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ("id", "title", "content")

# 방법2
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
        extra_kwargs = {
            'author' : {'read_only': True}
        }
        
# 방법3
# class ArticleCreateSerializer(serializers.ModelSerializer):
#     author = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Article
#         fields = '__all__'
        
#         extra_kwargs = {
#             'author': {'read_only': True}
#         }
    
    # def create(self, validated_data):
    #     author = self.context["request"].user
        
