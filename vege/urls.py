from django.urls import path
from . import views

urlpatterns = [
    path("recipes/", views.recipes, name="recipes"),
    path("delete-recipes/<id>/", views.delete_recipe, name="delete_recipe"),
    path("update-recipes/<id>/", views.update_recipe, name="update_recipe"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("register/", views.register, name="register"),
    path("students/", views.get_students, name="get_students"),
    path("student-marks/<student_id>", views.get_student_marks, name="get_student_marks"),
]
