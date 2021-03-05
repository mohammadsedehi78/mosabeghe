from django.urls import path
from django.contrib.auth.views import LogoutView

from index import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("login/", views.login_page, name='login_page'),
    path("logout/", LogoutView.as_view(next_page='/'), name='logout'),
    path("register/", views.register, name="register"),
    path("contact_us/", views.contact_us, name="contact_us"),
]
