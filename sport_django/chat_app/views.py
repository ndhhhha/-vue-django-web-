from django.shortcuts import render
from rest_framework import generics

from chat_app.serializer import ChatContentrSerializertoUser
from chat_app.models import ChatContent, Comment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user_app.utils import verify_token
from .serializer import ChatContentUserSerializer,ChatContentSerializer,CommentSerializer,ChatLikeSerializer

# Create your views here.
#获取文章列表
class ChatContentListView(generics.ListAPIView):
    queryset = ChatContent.objects.all()
    serializer_class = ChatContentUserSerializer


#文章添加
class ChatContentCreateView(APIView):
    def post(self,req):
        #获取请求头信息
        token = req.META.get('HTTP_AUTHORIZATION')
        #拿到用户ID
        data = verify_token(token)
        user_id = data.get('userid')

        #获取传来的用户ID
        user_id_req = int(req.data.get('user'))
        #判断用户ID是否一致
        if user_id != user_id_req:
            return Response({'message': '身份验证失败','code':1}, status=status.HTTP_401_UNAUTHORIZED)
        #进行序列化
        chat_content_ser = ChatContentSerializer(data=req.data)
        #进行数据校验
        if chat_content_ser.is_valid():
            #进行数据存储
            chat_content_ser.save()
            #返回数据
            return Response({
                'message': '发布成功',
                'code':0,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message':f'添加失败，请填写正确的数据',
                'errors':chat_content_ser.errors,
                'code':1,
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ChatDetailView(generics.RetrieveAPIView):
    '''
    获取文章详情接口
    '''
    queryset = ChatContent.objects.all()
    serializer_class = ChatContentSerializer

class PublicCommendView(APIView):
    '''
    提交评论api接口
    '''
    def post(self,req):
        #获取请求头信息
        token = req.META.get('HTTP_AUTHORIZATION')
        #拿到用户ID
        data = verify_token(token)
        user_id = data.get('userid')

        #获取传来的用户ID
        user_id_req = int(req.data.get('user'))
        #判断用户ID是否一致
        if user_id != user_id_req:
            return Response({'message': '身份验证失败','code':1}, status=status.HTTP_401_UNAUTHORIZED)
        #进行序列化
        commend_ser =  CommentSerializer(data = req.data)
        if commend_ser.is_valid():
            commend_ser.save()
        return Response({'message':'发布成功'},status=status.HTTP_200_OK)
    
class ChatLikeView(generics.UpdateAPIView):
    '''
    点赞接口
    '''
    queryset = ChatContent.objects.all()
    serializer_class = ChatLikeSerializer

class deleteChatView(generics.DestroyAPIView):
    '''
    删除文章接口
    '''
    queryset = ChatContent.objects.all()
    serializer_class = ChatContentrSerializertoUser