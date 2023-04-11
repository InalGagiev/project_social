from django.urls import path
from .views import *

urlpatterns = [
    #страница логина
    path('login/', LoginUser.as_view(), name='login'),
    #выход
    path('logout/', logout_user, name='logout'),
    #ссылка на регистрацию
    path('register/', SingUpView.as_view(), name='register'),
    #profile
    path('profile/<int:pk>', UserProfile.as_view(), name='profile')
]


