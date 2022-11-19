from django.contrib import admin
from django.urls import path
from cor_app.views import addTask,getStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTask/', addTask),
    path('getTask/<int:id>', getStudent)
]
