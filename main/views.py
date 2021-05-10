from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView

from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'categories': reverse('', request=request, format=format)
        # 'posts': reverse('post-list', request=request, format=format),
        # 'tags': reverse('tags-list', request=request, format=format)
    })


@api_view()
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    categories = serializer.data
    return Response(categories)

class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
