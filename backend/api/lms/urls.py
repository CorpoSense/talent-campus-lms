from django.urls import path
from .views import CourseView,CourseViewDetails

urlpatterns=[
    path("course/create/",CourseView.as_view(),name="post_get_update_delete_course"),
    path("course/<int:course_id>/",CourseViewDetails.as_view())
]

