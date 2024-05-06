from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("result/<int:result_id>", views.result_info, name="result_info"),
    path("result/", views.all_results, name="all_results"),
    path("arduino_data/", views.arduino_data, name="arduino_data"),
]
