from django.urls import path
from robots import views

urlpatterns = [
    path('get_report/', views.get_report, name='get_report'),
]
