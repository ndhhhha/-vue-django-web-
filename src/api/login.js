import request from '@/utils/request'

//注册API
export const RegisterService = (data) => request.post('/wnd/register/',data)
//登录API
export const LoginService = (data) => request.post('/wnd/login/',data)

