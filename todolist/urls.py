from django.urls import path

from todolist.views import register_user, show_tasks, login_user, logout_user

app_name = 'todolist'
urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    # path('create-task', create_task, name='create_task'),
    path('logout', logout_user, name='logout'),
]