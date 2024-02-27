from django.urls import path
from .views import LogoutView, RegisterView, LoginView,ProfileView

app_name = 'accounts'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='LogoutURL'),
    path('register/', RegisterView.as_view(), name='RegisterURL'),
    path('profile/', ProfileView.as_view(), name='ProfileURL'),
    path('', LoginView.as_view(), name='LoginURL'),
]
