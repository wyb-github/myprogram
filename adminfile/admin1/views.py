from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Goods
from .serializers import GoodsSerializer


from django.contrib.auth import authenticate,login
import json
# Create your views here.


# F B V
# def index(request):
#     return JsonResponse({'code':200,'msg':'hello word'})

# C B V

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class GoodsAPI(APIView):
    renderer_classes = [JSONRenderer]

    # 查看
    def get(self, requset, *args, **kwargs):
        data = Goods.objects.all()
        # 序列化
        goods = GoodsSerializer(data, many=True)
        print(goods.data[0]['cid'])
        order = Goods.objects.get(cid=goods.data[0]['cid'])
        print(order.name)

        return Response({'msg': goods.data})


# class TokenAuth(BaseAuthentication):
#     def authenticate(self,request):
#         token = request.META.get("HTTP_AUTHENTICATION",None)
#
#         if token:
#             obj = Token.objects.filter(key=token)
#             if obj:
#                 return None
#         raise exceptions.AuthenticationFailed('token 异常')

# class GoodsView(APIView):
#     renderer_classes = [JSONRenderer]
#     authentication_classes = [TokenAuth]
#     def get(self,request,*args,**kwargs):
#         goods = Goods.objects.all()
#         # 序列化
#         goods = GoodsSerializer(goods,many=True)
#         return Response({'code':200,'data':goods.data})
#
#     def post(self,request):
#         goodsser = GoodsSerializer(data=request.data)
#         # 验证
#         if goodsser.is_valid():
#             goodsser.save()
#             return Response(goodsser.data,status=status.HTTP_200_OK)
#         return Response(goodsser.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class GoodsOneView(APIView):
#     def put(self,request,*args,**kwargs):
#         goodsser = GoodsSerializer(data=request.data)
#         # 验证
#         if goodsser.is_valid():
#             goodsser.update(Goods.objects.filter(id=kwargs['id']).first(),request.data)
#             return Response(goodsser.data, status=status.HTTP_200_OK)
#         return Response(goodsser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,*args,**kwargs):
#         obj = Goods.objects.filter(id=kwargs['id']).first()
#         if obj:
#             obj.delete()
#             return Response({'msg':'ok'}, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# class Login(APIView):
#     def post(self,request):
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             login(request,user)
#             token = Token.objects.filter(user_id=user.id).first()
#             return Response({'msg':'ok','token':token.key})
#         else:
#             return Response({'msg': 'no'})