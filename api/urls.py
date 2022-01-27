from django.urls import path
from . import views
urlpatterns = [
    path('employeeview/',views.Emp_view),
]
