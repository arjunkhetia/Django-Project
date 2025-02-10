from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('<id>', views.user_by_id)
]