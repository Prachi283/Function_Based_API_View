from django.urls import path
from . import views
urlpatterns = [
    path('Employee_view/',views.Employee_view),
    path('Employee_view/<int:pk>',views.Employee_view),
]
