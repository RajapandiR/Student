from django.urls import path
from myapp import views

urlpatterns = [
    path('student/', views.StudentAPI.as_view()),
    path('student/<str:pk>/mark/', views.StudentMarkAPI1.as_view()),
    path('student/mark/add', views.StudentMarkAPI.as_view()),
    path('student/result/', views.Result.as_view())

]