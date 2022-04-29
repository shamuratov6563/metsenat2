from django.db.models import Sum
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer, SponsorSerializer, Student_sponsor, Student_sponsorSerializer
from .models import Student, Sponsor
from rest_framework.decorators import api_view

from dateutil.rrule import rrule, MONTHLY
from datetime import datetime


#Homiy arizasi uchun
class ApplicationApi(APIView):

    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorApi(ListAPIView):
    queryset =Sponsor.objects.all()
    serializer_class = SponsorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'id', 'data', 'phone_number', 'h_summa', 'organization_name', 'condition']
    filter_fields = ['date',  'payment_amount', 'condition']
    # permission_classes = (IsAdminUser,)

    # def total_allocated_money(self, pk):
    #     students = Student_sponsor.objects.all().filter(pk=pk)
    #     print(students)
    #     sum = 0
    #     for i in students:
    #         sum += i.spent_money
    #     print(sum)
    #     self.spent_money = sum


class SponsorUpdateApi(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    # permission_classes = (IsAdminUser,)


class StudentCreateApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsAdminUser,)


class StudentAPIView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'id', 'degree', 'contract_sum', 'university', 'allocated_money']
    filter_fields = ['degree', 'university']
    # permission_classes = (IsAdminUser,)


class StudentUpdateApi(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsAdminUser,)


@api_view(['GET'])
def dashboard(request):
    # permission_classes = (IsAdminUser,)

    for i in Student.objects.all():
        total_price_of_student = Student_sponsor.objects.filter(student__id=i.id).aggregate(Sum('spent_money'))['spent_money__sum']
        if total_price_of_student:
            i.allocated_money = total_price_of_student
            i.save()

    for i in Sponsor.objects.all():
        total_price_of_sponsor = Student_sponsor.objects.filter(sponsor__id=i.id).aggregate(Sum('spent_money'))['spent_money__sum']
        if total_price_of_sponsor:
            i.spent_money = total_price_of_sponsor
            i.save()

    # Total amount paid
    total_paid=Student_sponsor.objects.aggregate(Sum('spent_money'))['spent_money__sum']

    #Total requested amount
    students = Student.objects.all()
    b = 0
    for i in students:
        field_object = i._meta.get_field('contract_sum')
        field_value = field_object.value_from_object(i)
        b += field_value

    #number of sponsor
    first = Sponsor.objects.all().first().date
    last = Sponsor.objects.all().last().date

    def months(start_month, start_year, end_month, end_year):
        start = datetime(start_year, start_month, 1)
        end = datetime(end_year, end_month, 1)
        return [d for d in rrule(MONTHLY, dtstart=start, until=end)]

    sponsor = months(first.month, first.year, last.month, last.year)
    sponsor_monthly = []
    for i in sponsor:
        sponsor_monthly.append((i.strftime("%B/%Y"),
        Sponsor.objects.filter(date__year=i.year, date__month=i.month).count()))

    #number of students
    first = Student.objects.all().first().date
    last = Student.objects.all().last().date
    students = months(first.month, first.year, last.month, last.year)
    students_monthly = []
    for i in students:
        students_monthly.append((i.strftime("%B/%Y"),
        Student.objects.filter(date__year=i.year, date__month=i.month).count()))

    return Response({"Total paid money": total_paid, "Total requested amount": b, 'Money have to be paid': b-total_paid, "sponsors monthly": sponsor_monthly,
                     "students monthly": students_monthly})


class Student_sponsorCreateView(CreateAPIView):
    queryset = Student_sponsor.objects.all()
    serializer_class = Student_sponsorSerializer
    # permission_classes = (IsAdminUser,)


class Student_sponsorListView(ListAPIView):
    queryset = Student_sponsor.objects.all()
    serializer_class = Student_sponsorSerializer
    # permission_classes = (IsAdminUser,)


class Student_sponsorUpdateView(RetrieveUpdateAPIView):
    queryset = Student_sponsor.objects.all()
    serializer_class = Student_sponsorSerializer
    # permission_classes = (IsAdminUser,)



