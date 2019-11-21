from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Goods
from .serializers import GoodsSerializer

import  json
# Create your views here.


# F B V
def index(request):
    return JsonResponse({'code':200,'msg':'hello word'})

# C B V

class GoodsView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self,request,*args,**kwargs):
        goods = Goods.objects.all()
        # 序列化
        goods = GoodsSerializer(goods,many=True)
        return Response({'code':200,'data':goods.data})

    def post(self,request):
        goodsser = GoodsSerializer(data=request.data)
        # 验证
        if goodsser.is_valid():
            goodsser.save()
            return Response(goodsser.data,status=status.HTTP_200_OK)
        return Response(goodsser.errors,status=status.HTTP_400_BAD_REQUEST)

class GoodsOneView(APIView):
    def put(self,request,*args,**kwargs):
        goodsser = GoodsSerializer(data=request.data)
        # 验证
        if goodsser.is_valid():
            goodsser.update(Goods.objects.filter(id=kwargs['id']).first(),request.data)
            return Response(goodsser.data, status=status.HTTP_200_OK)
        return Response(goodsser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        obj = Goods.objects.filter(id=kwargs['id']).first()
        if obj:
            obj.delete()
            return Response({'msg':'ok'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)