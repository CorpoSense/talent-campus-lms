from django.urls import path
from .views import CourseView,CourseViewDetails,CourseUpdateView,CourseDeleteView

urlpatterns=[
    path("course/create/",CourseView.as_view(),name="post_get_update_delete_course"),
    path("course/<int:course_id>/",CourseViewDetails.as_view()),
    path("course/update/<int:course_id>/",CourseUpdateView.as_view()),
    path("course/delete/<int:course_id>/",CourseDeleteView.as_view(),name="delete_course")
]

