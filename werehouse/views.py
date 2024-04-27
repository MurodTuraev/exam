from django.shortcuts import render
from werehouse import serializers
from werehouse import models
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CategoryAPIView(APIView):
    def get(self, request, format=None):
        categories = models.CategoryModel.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)


class RawMaterialAPIView(APIView):
    def get(self, request, format=None):
        categories = models.RawMaterialModel.objects.all()
        serializer = serializers.RawMaterialSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryRawMaterialAPIView(APIView):
    def get(self, request, format=None):
        categories = models.CategoryRawMaterialModel.objects.all()
        serializer = serializers.CategoryRawMaterialSerializer(categories, many=True)
        return Response(serializer.data)


class WarehouseAPIView(APIView):
    def get(self, request, format=None):
        categories = models.WarehouseModel.objects.all()
        serializer = serializers.WarehouseSerializer(categories, many=True)
        return Response(serializer.data)


