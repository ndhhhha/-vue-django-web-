from rest_framework import serializers
from user_app.models import User
from rest_framework.response import Response
from rest_framework import status
# from chat_app.serializer import ChatContentSerializer
# from chat_app.serializer import ChatContentrSerializertoUser

#创建注册序列化器
class RegisterSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=11,min_length=11,required=True)
    password=serializers.CharField(max_length=32,min_length=6,required=True)
    # repassword=serializers.CharField(max_length=32,min_length=6,required=True)
    nickname=serializers.CharField(max_length=32,required=False)
    gender=serializers.IntegerField(required=False)
    introduction=serializers.CharField(max_length=20,required=False)
    # avatar=serializers.ImageField(required=False)后面进行添加
    created_at = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),required=False)
    #验证用户名是否存在
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("用户已存在")
            # return Response({'message': '用户已存在','code':1},status=status.HTTP_400_BAD_REQUEST)
        return value
    #验证确认密码是否一致
    # def validate_repassword(self,value):
    #     if self.initial_data['password'] != value:
    #         raise serializers.ValidationError("两次密码不一致")
    #     return value
    
    class Meta:
        model = User
        exclude = ('_password',)
        


# class UserDetailSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=11,min_length=11,required=True)
#     password=serializers.CharField(max_length=32,min_length=6,required=True)
#     nickname=serializers.CharField(max_length=32,required=False)
#     gender=serializers.IntegerField(required=False)
#     introduction=serializers.CharField(max_length=20,required=False)


    # class Meta:
    #     model = User,
    #     fields = "__all__"
#获取单个用户数据的序列化器
class UserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password=serializers.CharField(max_length=32,min_length=6,required=False)
    created_at = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),required=False)
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('updated_at','_password')

#获取单个用户数据的序列化器,但是没有密码
class UserDetailSerializeronpwd(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    # password=serializers.CharField(max_length=32,min_length=6,required=False)
    created_at = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),required=False)
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('updated_at','_password')

