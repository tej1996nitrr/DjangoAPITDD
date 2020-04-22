import pytest
from django.test  import  TestCase
from mixer.backend.django import mixer
from classroom.models import Student, ClassRoom
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
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
        User = get_user_model()
        self.our_user = User.objects.create_user(username="testuser", password="abcde")
        self.token_url = "http://localhost:8080/api-token-auth/"
        user_data = {"username": "testuser", "password": "abcde"}
        response = self.client.post(self.token_url, data=user_data)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])
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
        User = get_user_model()
        self.our_user = User.objects.create_user(username="testuser", password="abcde")
        self.token_url = "http://localhost:8080/api-token-auth/"
        user_data = {"username": "testuser", "password": "abcde"}
        response = self.client.post(self.token_url, data=user_data)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])
        student = mixer.blend(Student, first_name='Jeff')
        url = reverse('student_delete_api', kwargs={'pk':1})
        response = self.client.delete(url)
        assert response.status_code == 204
        assert Student.objects.count() == 0


class TestClassroomAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        # method 1
        # User = get_user_model()
        # self.our_user = User.objects.create(username="testuser", password="abcde")
        # self.token = Token.objects.create(user=self.our_user)
        # print(self.token.key, "token")
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        # method 2
        User = get_user_model()
        self.our_user = User.objects.create_user(username="testuser", password="abcde")
        self.token_url = "http://localhost:8080/api-token-auth/"
        user_data = {"username": "testuser", "password": "abcde"}
        response = self.client.post(self.token_url, data=user_data)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])

    def test_classroom_qs_works(self):
        classroom = mixer.blend(ClassRoom, student_capacity=20)
        classroom2 = mixer.blend(ClassRoom, student_capacity=27)
        url = reverse("classroom_query_api", kwargs={"student_capacity": 15})
        response = self.client.get(url, )
        assert response.status_code == 202
        assert response.data["classroom_data"] != []
        assert response.data["number_of_classes"] == 2
