from chat_app.models import ChatContent, Comment
from rest_framework import serializers
from user_app.serializer import UserDetailSerializeronpwd

#评论序列化
class ChatCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Comment
        fields = '__all__'  # 序列化所有字段

class ChatContentUserSerializer(serializers.ModelSerializer):
    #创建时间的格式化
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    #关联用户序列化
    user = UserDetailSerializeronpwd(read_only=True)
    comments = ChatCommentSerializer(many=True,read_only=True)
    # user = serializers.
    class Meta:
        model = ChatContent
        fields = ['id','title','content','created_at','updated_at','user','like','comments']  # 序列化所有字段





#评论序列化
class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)


    class Meta:
        model = Comment
        fields = '__all__'  # 序列化所有字段


#评论+用户序列化
class CommentUserSerializer(serializers.ModelSerializer):
        created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
        updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

        user = UserDetailSerializeronpwd(read_only=True)
        class Meta:
            model = Comment
            fields = ['content','created_at','updated_at','user']  # 序列化所有字段


class ChatContentSerializer(serializers.ModelSerializer):
    #创建时间的格式化
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    comments = CommentUserSerializer(many=True,read_only=True)
    
    class Meta:
        model = ChatContent
        fields = "__all__" 

class ChatLikeSerializer(serializers.ModelSerializer):
    '''
    点赞序列化函数
    '''

    class Meta:
        model = ChatContent
        fields = ['like']


class ChatContentrSerializertoUser(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = ChatContent
        fields = "__all__"