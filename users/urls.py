from django.urls import path
from .views import UserRegisterView, UserLoginView,ConfirmLogoutView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', ConfirmLogoutView.as_view(), name='logout'),

]
