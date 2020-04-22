from django.test import TestCase
from .models import Student, ClassRoom
from mixer.backend.django import mixer
import pytest
from hypothesis import given, strategies as st
from hypothesis.extra.django import TestCase
# Create your tests here.

pytestmark = pytest.mark.django_db  # not to save data to database


class TestStudentModel(TestCase):

    # def setUp(self):
    # self.student = Student.objects.create(average_score=30,first_name='Tom', last_name='Jerry', admission_number=1234, is_qualified=True)

    def test_student_creation(self):
        student = mixer.blend(Student, first_name="Tom")
        student_query = Student.objects.last()
        assert student_query.first_name == 'Tom'

    def test_string_return(self):
        student = mixer.blend(Student, first_name="Tom")
        assert str(student) == 'Tom'

    @given(st.floats(min_value=0, max_value=40))
    def test_grade_fail(self, fail_score):
        student = mixer.blend(Student, average_score=fail_score)
        student_query = Student.objects.last()
        assert student_query.get_grade() == 'Fail'

    @given(st.floats(min_value=40, max_value=70))
    def test_grade_pass(self, pass_score):
        student = mixer.blend(Student, average_score=pass_score)
        student_query = Student.objects.last()
        assert student_query.get_grade() == 'Pass'

    @given(st.floats(min_value=70, max_value=100))
    def test_grade_excellent(self,score):
        student = mixer.blend(Student, average_score=score)
        student_query = Student.objects.last()
        assert student_query.get_grade() == 'Excellent'

    @given(st.floats(min_value=100))
    def test_grade_error(self, error_grade):
        student = mixer.blend(Student, average_score=error_grade)
        student_query = Student.objects.last()
        assert student_query.get_grade() == 'Error'


class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(ClassRoom, name='Physics')
        classroom_query = ClassRoom.objects.last()
        assert classroom_query.name == "Physics"
        assert str(classroom) == "Physics"




