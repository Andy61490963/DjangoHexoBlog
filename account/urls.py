from django.urls import include, path
from . import views

urlpatterns = [
    path('Login',views.login_user, name="login"),
    path('Logout',views.logout_user, name="logout"),
    path('Register',views.register_user, name="register"),
]
