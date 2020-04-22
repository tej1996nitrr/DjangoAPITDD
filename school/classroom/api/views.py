from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from ..models import Student


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()