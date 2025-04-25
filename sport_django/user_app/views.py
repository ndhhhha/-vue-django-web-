from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_app.models import User
from rest_framework import generics

from user_app.serializer import RegisterSerializer,UserDetailSerializer
from .utils import generate_token,verify_token

from chat_ap.serizlizer import UserChatContentSerializer2

# Create your views here.   
class LoginView(APIView):
    def post(self, request):
        '''
        登录接口
        '''
        # 1、获取请求数据
        username = request.data.get('username')
        password = request.data.get('password')
        #2、数据库进行查询
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': '用户不存在','code':1}, status=status.HTTP_404_NOT_FOUND)
        # 3、进行登录逻辑处理
        if user.check_password(password):
            #4、 登录成功，返回用户信息
            return Response({'message': '登录成功','data':{
                'id':user.id,
                # 'nickname':user.nickname,
                # 'gender':user.gender,
                # 'introduction':user.introduction,
                'token':generate_token({'username':user.username,'userid':user.id}),
            },'code':0}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '用户名或密码错误','code':1}, status=status.HTTP_401_UNAUTHORIZED)
        
class RegisterView(APIView):
    '''
    注册接口
    '''
    def post(self,req):
        #1、创建序列化器
        register_ser = RegisterSerializer(data=req.data)
        #2、进行数据校验
        if register_ser.is_valid():
            #3、进行数据存储
            register_ser.save()
            #4、返回数据
            return Response({
                'code':0,
                'message': '注册成功',
                }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message':f'注册失败，请填写正确的数据,用户名重复或密码违规',
                'errors':register_ser.errors,
                'code':1,
            }, status=status.HTTP_400_BAD_REQUEST)
        

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserofChatView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserChatContentSerializer2