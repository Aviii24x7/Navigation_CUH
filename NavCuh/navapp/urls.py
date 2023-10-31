from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="starting_page"),
    path("depts", views.AllDeptView.as_view(), name="all-dept-page"),
    path("depts/<slug:slug>", views.SingleDeptView.as_view(), name="all-teachers-page"),
]
