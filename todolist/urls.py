from django.urls import path

from todolist.views import add_task, delete_ajax, register_user, show_json, show_tasks, login_user, logout_user, create_task, update, delete, show_tasks_ajax, update_ajax

app_name = 'todolist'
urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    path('create-task', create_task, name='create_task'),
    path('logout', logout_user, name='logout'),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),

    path('ajax', show_tasks_ajax, name='show_tasks_ajax'),
    path('update_ajax/<int:id>', update_ajax, name="update_ajax"),
    path('delete_ajax/<int:id>', delete_ajax, name="delete_ajax"),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
]