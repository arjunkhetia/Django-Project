from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    # path('<int:id>', views.userid_int),
    # path('<uuid:id>', views.userid_uuid),
    # path('<str:id>', views.userid_str),
    path('ui', views.user_home),
    path('user', views.user_user),
]