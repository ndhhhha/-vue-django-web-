import request from '@/utils/request'

//获取单个用户数据
export const getUserInfoService = (pk)=> request.get(`/wnd/user/${pk}/`)

//修改单个用户数据
export const UpdateUserInfoService = (pk,data)=> request.put(`/wnd/user/${pk}/`,data)

//请求单个用户评论
export const getUserChatService = (id)=> request.get(`/wnd/userchats/${id}/`)