from django.urls import path
from .views import StudentListAPIView, StudentCreateAPIView, StudentDeleteAPIView, StudentRetrieveAPIView, ClassRoomAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name='student_list_api'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create_api'),
    path('student/<int:pk>/', StudentRetrieveAPIView.as_view(), name='student_retrieve_api'),
    path('student/<int:pk>/delete/', StudentDeleteAPIView.as_view(), name='student_delete_api'),
    path('classroom/<int:student_capacity>/', ClassRoomAPIView.as_view(), name='classroom_query_api'),


]