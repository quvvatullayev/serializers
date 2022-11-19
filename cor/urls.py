from django.contrib import admin
from django.urls import path
from cor_app.views import addTask,getStudent,deletTask,updateTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTask/', addTask),
    path('getTask/<int:id>', getStudent),
    path('deletTask/<int:id>', deletTask),
    path('updateTask/<int:id>',updateTask)
]
