from django.urls import path, re_path

from . import views

urlpatterns = [
	path('api/users', views.UserListApiView.as_view()),
	path('api/users/<id>', views.UserSearchApiView.as_view()),
	path('api/users/new/', views.UserCreateApiView.as_view()),
] 