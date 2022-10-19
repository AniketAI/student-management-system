from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from smsapp.models import CustomUser, Staffs, Courses, Students, SessionYearModel,TODO



def student_home(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     todos = TODO.objects.filter(user = user).order_by('priority')

    todos = TODO.objects.all()
    student_details = CustomUser.objects.filter(user_type = request.user.user_type, id = request.user.id )

    context={'todos' : todos,'student_details':student_details}
    return render(request, "studenttemp/student_home_template.html", context)