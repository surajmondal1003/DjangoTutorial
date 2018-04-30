from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from first_app.models import Topic,Webpage,AccessRecord,users_test
from .serializers import Users_testDetailSerializer,Users_testListSerializer,Users_testCreateSerializer







class UsersCreateAPIView(CreateAPIView):
    queryset=users_test.objects.order_by('first_name')
    serializer_class = Users_testCreateSerializer

    permission_classes = [IsAuthenticated,IsAdminUser]


class UsersListAPIView(ListAPIView):
    queryset=users_test.objects.order_by('first_name')
    serializer_class = Users_testListSerializer

class UsersDetailAPIView(RetrieveAPIView):
    queryset = users_test.objects.order_by('first_name')
    serializer_class = Users_testDetailSerializer

class UsersUpdateAPIView(RetrieveUpdateAPIView):
    queryset = users_test.objects.order_by('first_name')
    serializer_class = Users_testDetailSerializer



class UsersDeleteAPIView(DestroyAPIView):
    queryset = users_test.objects.order_by('first_name')
    serializer_class = Users_testDetailSerializer
