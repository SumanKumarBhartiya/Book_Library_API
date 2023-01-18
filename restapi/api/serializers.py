from django.contrib.auth.models import User
from restapi.models import Book,AuthorInfo,Review,Issue_Book,Student,Penalty
from rest_framework import serializers
from django.utils.timezone import now

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model=User
        fields=['id','username','email','days_since_joined']

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields='__all__'

class AuthorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=AuthorInfo
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review
        fields='__all__'

class IssueBookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Issue_Book
        fields='__all__'

class PenaltySerializer(serializers.ModelSerializer):

    class Meta:
        model=Penalty
        fields='__all__'

