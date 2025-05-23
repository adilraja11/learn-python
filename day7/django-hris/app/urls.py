from django.urls import path
from .views import EmployeeListView, EmployeeDetailView

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("<str:id>/", EmployeeDetailView.as_view(), name="employee-detail"),
]
