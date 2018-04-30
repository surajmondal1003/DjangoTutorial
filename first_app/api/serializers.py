from rest_framework.serializers import ModelSerializer
from first_app.models import Topic,Webpage,AccessRecord,users_test

class Users_testCreateSerializer(ModelSerializer):
    class Meta:
        model=users_test
        fields=[
            'first_name',
            'last_name',
            'email'
        ]


class Users_testListSerializer(ModelSerializer):
    class Meta:
        model=users_test
        fields=[
            'id',
            'first_name',

        ]

class Users_testDetailSerializer(ModelSerializer):
    class Meta:
        model=users_test
        fields=[
            'id',
            'first_name',
            'last_name',
            'email'
        ]