from .utils import verify_token
from django.http import JsonResponse
from rest_framework import status

#定义中间件用于判断用户是否登录
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #获取请求路径是否包含wnd/login和wnd/register
        if request.path.startswith(('/wnd/login/', '/wnd/register/','/admin/','/media/')):
            return self.get_response(request)
        # 获取请求头中的token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not verify_token(token):
            # 验证token失败
            return JsonResponse({
                'message': '请登录',
                  'code': 1,
                  }, status=status.HTTP_401_UNAUTHORIZED,
                  #正常来说jsonResponse不显示中文，所以要进行转码
                  json_dumps_params={'ensure_ascii': False})
        # 验证token成功
        return self.get_response(request)