from django.contrib import admin
from django.urls import path,include
from cor_app.views import Create_task,update_task,Remov_task,Get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTask/', Create_task.as_view()),
    path('updateTask/<int:id>', update_task),
    path('removTask/<int:id>', Remov_task.as_view()),
    path('Get/<int:id>', Get_all.as_view()),
    path('auth', include('rest_framework.urls'))
]
