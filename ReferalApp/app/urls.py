from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views.HomeView import HomeView
from .views.ProfileView import ProfileView
from .views.ApiDRF import BindingInviteListView

urlpatterns = [
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/list', BindingInviteListView.as_view(), name='binding_invite_list'),

    path('', HomeView.as_view(), name='home_view'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
]