import pytest
from django.test  import  TestCase
from mixer.backend.django import mixer
from classroom.models import Student, ClassRoom
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
pytestmark = pytest.mark.django_db  # not to save data to database

class TestStudentAPIViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        print(self.client,'client')


    def test_student_list_view(self):
        student = mixer.blend(Student, first_name='Jeff')
        url = reverse('student_list_api')
        response = self.client.get(url)
        print(response,"response")
        assert response.json != None
        assert len(response.json())==1
        assert response.status_code == 200
