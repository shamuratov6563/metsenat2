from django.contrib import admin
from .models import Sponsor, Student, University, Student_sponsor


admin.site.register([Sponsor, Student, University, Student_sponsor])


