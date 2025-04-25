import request from '@/utils/request'

//获取文章列表
export const getChatListService = () => request.get('/chatcontents/')
//发布文章
export const createChatService = (data) => request.post('/chatcontentsadd/', data)

//获取文章详情
export const getChatDetailService = (id) => request.get(`/chatdetail/${id}/`)

//发布评论
export const createCommendService = (data) => request.post('/commendadd/',data)

//点赞接口
export const chatLikeService = (id,data) => request.put(`/chatlike/${id}/`,data)

//删除文章接口
export const deleteChatService = (id)=> request.delete(`/chatdelete/${id}/`)