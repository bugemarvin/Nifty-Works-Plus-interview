from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from blog.models import Blog

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def BlogListView(request):
        pass

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def BlogDetailView(request):
        pass