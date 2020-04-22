from rest_framework.generics import ListAPIView,CreateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import StudentSerializer
from ..models import Student


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
