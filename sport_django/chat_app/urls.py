from django.urls import path
from . import views

urlpatterns = [
    path('chatcontents/', views.ChatContentListView.as_view()),
    path('chatcontentsadd/', views.ChatContentCreateView.as_view()),
    path('chatdetail/<int:pk>/',views.ChatDetailView.as_view()),
    path('commendadd/',views.PublicCommendView.as_view()),
    path('chatlike/<int:pk>/',views.ChatLikeView.as_view()),
    path('chatdelete/<int:pk>/',views.deleteChatView.as_view())
]