from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('update_task/<str:Id>', views.update_task, name="update_task"),
    path('delete_task/<str:Id>',views.delete_task, name='delete_task'),
]