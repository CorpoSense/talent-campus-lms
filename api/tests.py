from django.test import TestCase
from django.contrib.auth.models import User
from .models import Instructor, CourseCategorie, Course
from datetime import datetime

class CourseModelTest(TestCase):
    
    def setUp(self):
        # Create a user and instructor
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.instructor = Instructor.objects.create(user=self.user)

        # Create a category
        self.category1 = CourseCategorie.objects.create(categorieName='Programming')
        self.category2 = CourseCategorie.objects.create(categorieName='Data Science')

    def test_course_creation(self):
        # Create a course
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch.',
            image='http://example.com/image.png',
            instructor=self.instructor,
            rating=4.5,
            status='published'
        )
        course.categories.add(self.category1, self.category2)

        # Test that the course was created successfully
        self.assertEqual(course.title, 'Python for Beginners')
        self.assertEqual(course.description, 'Learn Python from scratch.')
        self.assertEqual(course.image, 'http://example.com/image.png')
        self.assertEqual(course.instructor, self.instructor)
        self.assertEqual(course.rating, 4.5)
        self.assertEqual(course.status, 'published')
        self.assertEqual(course.categories.count(), 2)
        self.assertIn(self.category1, course.categories.all())
        self.assertIn(self.category2, course.categories.all())

    def test_course_str_representation(self):
        # Create a course
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch.',
            image='',
            instructor=self.instructor,
        )
        # Test the string representation
        self.assertEqual(str(course), 'Python for Beginners')

    def test_course_default_values(self):
        # Create a course with minimal data
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch.',
            instructor=self.instructor,
        )
        # Test the default values
        self.assertEqual(course.rating, 1.0)
        self.assertEqual(course.status, 'draft')

    def test_course_ordering(self):
        # Create multiple courses
        course1 = Course.objects.create(
            title='Course 1',
            description='First course',
            instructor=self.instructor,
        )
        course2 = Course.objects.create(
            title='Course 2',
            description='Second course',
            instructor=self.instructor,
        )
        # Test the ordering
        courses = Course.objects.all()
        self.assertEqual(courses[0], course2)
        self.assertEqual(courses[1], course1)

    def test_course_instructor_relationship(self):
        # Create a course
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch.',
            instructor=self.instructor,
        )
        # Test the relationship with instructor
        self.assertEqual(course.instructor, self.instructor)
        self.assertEqual(self.instructor.courses.count(), 1)
        self.assertIn(course, self.instructor.courses.all())

    def test_course_categories_relationship(self):
        # Create a course and assign categories
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch.',
            instructor=self.instructor,
        )
        course.categories.add(self.category1, self.category2)

        # Test the relationship with categories
        self.assertEqual(course.categories.count(), 2)
        self.assertIn(self.category1, course.categories.all())
        self.assertIn(self.category2, course.categories.all())
        self.assertEqual(self.category1.courses.count(), 1)
        self.assertIn(course, self.category1.courses.all())

# More detailed tests
# from django.core.exceptions import ValidationError
# from django.db.utils import IntegrityError

# class CourseModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create a user
#         cls.user = User.objects.create_user(username='testuser', password='12345')
        
#         # Create an instructor
#         cls.instructor = Instructor.objects.create(user=cls.user)
        
#         # Create a course category
#         cls.category = CourseCategorie.objects.create(categorieName='Test Category')
        
#         # Create a course
#         cls.course = Course.objects.create(
#             title='Test Course',
#             description='This is a test course',
#             instructor=cls.instructor,
#             rating=4.5,
#             status='published'
#         )
#         cls.course.categories.add(cls.category)

#     def test_course_creation(self):
#         self.assertTrue(isinstance(self.course, Course))
#         self.assertEqual(self.course.__str__(), self.course.title)

#     def test_course_fields(self):
#         self.assertEqual(self.course.title, 'Test Course')
#         self.assertEqual(self.course.description, 'This is a test course')
#         self.assertEqual(self.course.instructor, self.instructor)
#         self.assertEqual(self.course.rating, 4.5)
#         self.assertEqual(self.course.status, 'published')

#     def test_course_categories(self):
#         self.assertEqual(self.course.categories.count(), 1)
#         self.assertEqual(self.course.categories.first(), self.category)

#     def test_course_instructor_relationship(self):
#         self.assertEqual(self.instructor.courses.first(), self.course)

#     def test_course_default_values(self):
#         new_course = Course.objects.create(
#             title='New Course',
#             description='New course description',
#             instructor=self.instructor
#         )
#         self.assertEqual(new_course.rating, 1.0)
#         self.assertEqual(new_course.status, 'draft')

#     def test_course_status_choices(self):
#         valid_statuses = ['draft', 'published', 'expired']
#         for status in valid_statuses:
#             self.course.status = status
#             self.course.full_clean()  # This should not raise a ValidationError

#         self.course.status = 'invalid_status'
#         with self.assertRaises(ValidationError):
#             self.course.full_clean()

#     def test_course_ordering(self):
#         new_course = Course.objects.create(
#             title='Newer Course',
#             description='Newer course description',
#             instructor=self.instructor
#         )
#         courses = Course.objects.all()
#         self.assertEqual(courses[0], new_course)
#         self.assertEqual(courses[1], self.course)

#     def test_course_image_null(self):
#         self.course.image = None
#         self.course.save()
#         self.assertIsNone(self.course.image)

#     def test_course_instructor_deletion(self):
#         self.user.delete()
#         with self.assertRaises(Course.DoesNotExist):
#             Course.objects.get(id=self.course.id)

#     def test_max_length_constraints(self):
#         max_length_course = Course.objects.create(
#             title='A' * 100,  # Max length for title
#             description='B' * 1000,  # Max length for description
#             instructor=self.instructor
#         )
#         max_length_course.full_clean()  # This should not raise a ValidationError

#         with self.assertRaises(ValidationError):
#             Course.objects.create(
#                 title='A' * 101,  # Exceeds max length for title
#                 description='Test description',
#                 instructor=self.instructor
#             ).full_clean()

#         with self.assertRaises(ValidationError):
#             Course.objects.create(
#                 title='Test title',
#                 description='B' * 1001,  # Exceeds max length for description
#                 instructor=self.instructor
#             ).full_clean()

#     def test_course_without_instructor(self):
#         with self.assertRaises(IntegrityError):
#             Course.objects.create(
#                 title='Course without instructor',
#                 description='This should fail'
#             )