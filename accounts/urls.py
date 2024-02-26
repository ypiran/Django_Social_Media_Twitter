from django.urls import path
from .views import LogoutView, RegisterView, LoginView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='LogoutURL'),
    path('register/', RegisterView.as_view(), name='RegisterURL'),
    path('', LoginView.as_view(), name='LoginURL'),
]
