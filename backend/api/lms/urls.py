from django.urls import path
from .views import CourseView

urlpatterns=[
    path("course/create/",CourseView.as_view(),name="post_get_update_delete_profile")
]

