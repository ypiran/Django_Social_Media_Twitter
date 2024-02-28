from django.urls import path
from .views import LogoutView, RegisterView, LoginView

app_name = 'accounts'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='LogoutURL'),
    path('register/', RegisterView.as_view(), name='RegisterURL'),
    path('', LoginView.as_view(), name='LoginURL'),
]
