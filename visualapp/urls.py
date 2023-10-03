from django.urls import path
from .views import Postlist,CreateUserView

urlpatterns = [
    path("", Postlist.as_view(), name="postlist"),
    path("create_user/",CreateUserView.as_view(),name="createuser")
]

