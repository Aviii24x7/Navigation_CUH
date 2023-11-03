from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="starting_page"),
    path("schools", views.AllSchoolView.as_view(), name="all-school-page"),
    path("school/<slug:slugy>", views.AllDeptView.as_view(), name="all-dept-page"),
    path("department/<slug:slug>", views.AllTeacherView.as_view(), name="all-teachers-page"),
]
