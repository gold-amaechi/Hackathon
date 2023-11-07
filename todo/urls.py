from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

app_name = 'todo'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task/add/', TaskCreate.as_view(), name='task-add'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
]
