from django.urls import path, include
from rest_framework import routers 
from . import views

router = routers.DefaultRouter() 
router.register('tasks', views.TaskView) 
router.register('users', views.UserView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]