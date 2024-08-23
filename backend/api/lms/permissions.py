from django.contrib.auth.models import Group,Permission

#import course model
from .models import Course,User

# Create Groups for each role
admin_group, _ = Group.objects.get_or_create(name='Administrator')
course_creator_group, _ = Group.objects.get_or_create(name='Course Creator')
instructor_group, _ = Group.objects.get_or_create(name='Instructor')
reporter_group, _ = Group.objects.get_or_create(name='Reporter')
learner_group, _ = Group.objects.get_or_create(name='Learner')


## define permissions for each role :
# adminstrator permissions
admin_permissions = Permission.objects.all()
admin_group.permissions.set(admin_permissions)


# course creator permissions 
course_creator_permissions = Permission.objects.filter(
    content_type_app_label="lms",
    codename__in=[
        'add_course', 'change_course', 'delete_course', 
        'manage_enrollments'
    ]
)

course_creator_group.permissions.set(course_creator_permissions)

# instructor permissions
instructor_permissions = Permission.objects.filter(
    content_type_app_label="lms",
    codename_in=[
        'change_course', 'add_assessment', 'change_assessment', 
        'monitor_progress'
    ]
)

instructor_group.permissions.set(instructor_permissions)


# Reporter: Focus on analytics
reporter_permissions = Permission.objects.filter(
    content_type__app_label='your_app_name',
    codename__in=[
        'view_user_progress', 'export_reports'
    ]
)
reporter_group.permissions.set(reporter_permissions)

# Learner: Basic access
learner_permissions = Permission.objects.filter(
    content_type__app_label='your_app_name',
    codename__in=[
        'view_course', 'access_course_materials', 'participate_in_course'
    ]
)
learner_group.permissions.set(learner_permissions)