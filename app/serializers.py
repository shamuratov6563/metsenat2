from django.db.models import Sum
from rest_framework import serializers
from .models import Student, Sponsor, University, Student_sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    # students = Student.objects.first()
    # Student_sponsors = Student_sponsor.objects.filter(sponsor=students.id)
    # students.allocated_money = Student_sponsors.spent_money
    # students.save()
    # allocated_money=Student_sponsor.objects.aggregate(allocated_money=Sum('student_sponsor_')

    class Meta:
        model = Student
        fields = "__all__"


class Student_sponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student_sponsor
        fields = "__all__"



