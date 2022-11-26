from django.contrib import admin
from django.urls import path
from cor_app.views import create_task,update_task,remov_task,get_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTask/', create_task),
    path('updateTask/<int:id>', update_task),
    path('removTask/<int:id>', remov_task),
    path('getTask/<int:id>', get_task)
]
