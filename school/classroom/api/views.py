from rest_framework.generics import ListAPIView,CreateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import StudentSerializer, ClassRoomSerializer
from ..models import Student, ClassRoom
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class ClassRoomAPIView(APIView):
    serializer_class = ClassRoomSerializer
    model = ClassRoom

    def get(self, *args, **kwargs):
        url_number = self.kwargs.get('student_capacity')
        classroom_qs = ClassRoom.objects.filter(student_capacity__gte=url_number)
        serialized_data = ClassRoomSerializer(classroom_qs, many=True)
        number_of_classes = classroom_qs.count()
        if serialized_data.is_valid:
            return Response(
                {
                    "classroom_data": serialized_data.data,
                    "number_of_classes": number_of_classes,
                },
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                {"Error": "Could not serialize data"},
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            )
