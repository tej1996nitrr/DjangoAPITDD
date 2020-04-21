from django.test import TestCase
from .models import Student
from mixer.backend.django import mixer

# Create your tests here.


class TestStudentModel(TestCase):

    # def setUp(self):
    # self.student = Student.objects.create(average_score=30,first_name='Tom', last_name='Jerry', admission_number=1234, is_qualified=True)

    def test_student_creation(self):
        student = mixer.blend(Student, first_name="Tom")
        student_query = Student.objects.last()
        self.assertEqual(student_query.first_name, 'Tom')

    def test_string_return(self):
        student = mixer.blend(Student, first_name="Tom")
        self.assertEqual(str(student), 'Tom')

    def test_grade_fail(self):
        student = mixer.blend(Student, average_score=10)
        student_query = Student.objects.last()
        self.assertEqual(student_query.get_grade(), 'Fail')

    def test_grade_pass(self):
        student = mixer.blend(Student, average_score=50)
        student_query = Student.objects.last()
        self.assertEqual(student_query.get_grade(), 'Pass')

    def test_grade_excellent(self):
        student = mixer.blend(Student, average_score=80)
        student_query = Student.objects.last()
        self.assertEqual(student_query.get_grade(), 'Excellent')




