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

    def test_student_create_view(self):
        data_required = {
        "first_name": "Tom",
        "last_name": "Jerry",
        "admission_number": 12,
        "is_qualified": False,
        "average_score": 30,
        "username": "Tommy"
        }
        url  = reverse('student_create_api')
        respose = self.client.post(url,data=data_required)
        assert respose.json() != None
        assert respose.status_code == 201
        assert Student.objects.count()==1

    def test_student_detail_view(self):
        student = mixer.blend(Student, first_name='Jeff')
        url = reverse('student_retrieve_api', kwargs={'pk':1})
        response = self.client.get(url)
        assert response.json != None
        assert len(response.json()) == 6
        assert response.status_code == 200
        assert response.json()['first_name'] =='Jeff'

    def test_student_delete_view(self):
        student = mixer.blend(Student, first_name='Jeff')
        url = reverse('student_delete_api', kwargs={'pk':1})
        response = self.client.delete(url)
        assert response.status_code == 204
        assert Student.objects.count() == 0

