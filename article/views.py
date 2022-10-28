from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from article.models import Article
from article.serializers import ArticleCreateSerializer, ArticleSerializer

class ArticleView(APIView):
    def get(self, reuqest):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        # 방법 1 
        # if serializer.is_valid():
        #     serializer.save(author=request.user)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 방법 2
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        