from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app.views import CreateUserView, PostListView,PostRetriveView,PostViewSet

router = routers.DefaultRouter()
router.register('posts',PostViewSet,basename='posts')

urlpatterns = [
   
    path('auth/',include('djoser.urls.jwt')),
    path('',include(router.urls)),
    path('list-post/',PostListView.as_view(),name='list-post'),
    path('detail-post/<str:pk>/', PostRetriveView.as_view(),name='detail-post'),
    path('register/',CreateUserView.as_view(),name='register'),
]