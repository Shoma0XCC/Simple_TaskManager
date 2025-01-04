from django.urls import path
from main.views import UpdateTask, creat, Detail

urlpatterns = [
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('details/<int:pk>/', Detail.as_view(), name='details_task'),
    path('', creat, name='creat'),

]


