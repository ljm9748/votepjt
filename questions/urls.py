from django.urls import path
from . import views

app_name='questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:pk>/<int:pick_num>/pick/', views.pick, name='pick'),
    
]
