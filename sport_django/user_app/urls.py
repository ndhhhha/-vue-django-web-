from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('user/<int:pk>/',views.UserDetailView.as_view()),
    # path('user/userchats/',views.use)
    path('userchats/<int:pk>/',views.UserofChatView.as_view())
]