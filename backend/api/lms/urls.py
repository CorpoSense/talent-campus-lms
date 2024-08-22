from django.urls import path
from .views import CourseView,CourseViewDetails,CourseUpdateView,CourseDeleteView,CourseEnrollementView,GetEnrolledCoursesView

urlpatterns=[
    path("course/create/",CourseView.as_view(),name="post_get_update_delete_course"),
    path("course/<int:course_id>/",CourseViewDetails.as_view()),
    path("course/update/<int:course_id>/",CourseUpdateView.as_view()),
    path("course/delete/<int:course_id>/",CourseDeleteView.as_view(),name="delete_course"),
    path("course/enroll/<int:course_id>/",CourseEnrollementView.as_view()),
    path("course/my_courses/",GetEnrolledCoursesView.as_view(),name="user_enrolled_courses")
]


