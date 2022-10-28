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
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)