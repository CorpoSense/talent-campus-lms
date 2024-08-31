from django.urls import path
from .views import CourseView,CourseViewDetails,CourseUpdateView,CourseDeleteView,CourseEnrollementView,GetEnrolledCoursesView,RatingView,EnrolledCourseViewDetails,CourseDiscussionsView,CreateDiscussionCourseView,AssessmentView,AddDiscussionCommentView,CreateQuizView,UpdateQuizView,QuizDeleteView,DeleteAssessementView

urlpatterns=[
    path("course/create/",CourseView.as_view(),name="post_get_update_delete_course"),
    path("course/<int:course_id>/",CourseViewDetails.as_view()),
    path("course/update/<int:course_id>/",CourseUpdateView.as_view()),
    path("course/delete/<int:course_id>/",CourseDeleteView.as_view(),name="delete_course"),
    path("course/enroll/<int:course_id>/",CourseEnrollementView.as_view()),
    path("course/my_courses/",GetEnrolledCoursesView.as_view(),name="user_enrolled_courses"),
    path("course/rate/",RatingView.as_view(),name="rate_course"),
    path("enrollement/<int:enroll_id>/",EnrolledCourseViewDetails.as_view(),name="enrollement details"),
    path("course/discussions/<int:course_id>/",CourseDiscussionsView.as_view(),name="course_discuusion"),
    path("discussion/add/<int:course_id>/",CreateDiscussionCourseView.as_view(),name="create_disussion_course"),
    path("discussion/comment/<int:discussion_id>/",AddDiscussionCommentView.as_view(),name="add_discussion_comment"),
    path("quiz/add/<int:course_id>/",CreateQuizView.as_view(),name="create_quiz"),
    path("quiz/update/<int:quiz_id>/",UpdateQuizView.as_view()),
    path("quiz/delete/<int:quiz_id>/",QuizDeleteView.as_view()),
    path("assessement/<int:course_id>/",AssessmentView.as_view()),
    path("assessement/delete/<int:asse_id>/",DeleteAssessementView.as_view())
]



