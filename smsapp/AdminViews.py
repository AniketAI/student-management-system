from django import views
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from smsapp.models import CustomUser, Staffs, Courses, Students, SessionYearModel, Semesters, TODO
from .forms import AddStudentForm, EditStudentForm, TODOForm


def adminmain_home(request):
    todos = TODO.objects.filter(user = request.user).order_by('priority')
    students = Students.objects.all()
    context = {"todos":todos,
               "students":students}
    return render(request, "admintemp/main_content.html",context)

def show_admin_data(request):
    show_data = CustomUser.objects.all()
    context = {"show_data":show_data}
    return render(request, "admintemp/show_admin_data.html", context)

def show_semester_data(request):
    show_sem_data = Semesters.objects.all()
    context = {"show_sem_data":show_sem_data}
    return render(request, "admintemp/show_semester_data.html", context)



def add_hod(request):
    return render(request, "admintemp/add_hod_template.html")


def add_hod_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_hod')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.adminmain.address = address
            user.save()
            messages.success(request, "hod Added Successfully!")
            return redirect('add_hod')
        except:
            messages.error(request, "Failed to Add hod!")
            return redirect('add_hod')

def add_mainstaff(request):
    return render(request, "admintemp/add_mainstaff_template.html")


def add_mainstaff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_mainstaff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.staffs.address = address
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_mainstaff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_mainstaff')



def add_maincourse(request):
    return render(request, "admintemp/add_maincourse_template.html")


def add_maincourse_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_maincourse')
    else:
        course = request.POST.get('course')
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_maincourse')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_maincourse')

def add_session(request):
    return render(request, 'admintemp/add_sessions.html')

def add_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_course')
    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Session Year added Successfully!")
            return redirect("add_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect("add_session")


def add_mainsemester(request):
    return render(request, "admintemp/add_mainsem.html")

def add_mainsemester_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_mainsemester')
    else:
        sem = request.POST.get('semester')
        sections = request.POST.get('section')
        main_sem = Semesters.objects.filter(semester=sem, section=sections)
        if main_sem.exists():
            messages.success(request, "Already exists")
            return redirect('add_mainsemester')
        else:
            try:
                sem_model = Semesters(semester=sem, section=sections)
                sem_model.save()
                messages.success(request, "Semester & Class Added Successfully!")
                return redirect('add_mainsemester')
            except:
                messages.error(request, "Failed to Add Semester & Class!")
                return redirect('add_mainsemester')


def delete(request, id):
    # data = Semesters.objects.get(id=id) 
    data = get_object_or_404(Semesters, id=id) 
    data.delete()
    return redirect('show_semester_data')


def maindelete(request, id):
    # data = Semesters.objects.get(id=id) 
    data = get_object_or_404(CustomUser, id=id) 
    data.delete()
    return redirect('show_admin_data')


def add_mainstudent(request):
    form = AddStudentForm()
    context = {
        "form": form
    }
    return render(request, 'admintemp/add_mainstudent.html', context)


def add_mainstudent_save(request, **extrafields):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_mainstudent')
    else:
        # try:
        #         profile = request.user.semesters_id
        # except Semesters.DoesNotExist:
        #         profile = Semesters(id=request.user)

        form = AddStudentForm(request.POST, request.FILES)
        
        

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            semesters_id = form.cleaned_data['semesters_id']
            semesters_section_id = form.cleaned_data['semesters_section_id']
            session_year_id = form.cleaned_data['session_year_id']
            course_id = form.cleaned_data['course_id']
            gender = form.cleaned_data['gender']

            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

        
            # try:
                user = CustomUser.objects.create(username=username,password=password, email=email, first_name=first_name, last_name=last_name, user_type=4)
                
                user.students.address = address

                course_obj = Courses.objects.get(id=course_id)
                
                user.students.course_id = course_obj

                session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id = session_year_obj

                user.students.gender = gender
                user.students.profile_pic = profile_pic_url

                semesters_obj = Semesters.objects.filter(id=semesters_id)
                user.students.semesters = semesters_obj

                
                user.students.section = semesters_section_id
                user.save()

    
                messages.success(request, "Student Added Successfully!")
                return redirect('add_mainstudent')
            # except:
            #     messages.error(request, "Failed to Add Student!")
            #     return redirect('add_mainstudent')
        else:
            return redirect('add_mainstudent')






# todo views 

def show_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'todo/addtodo.html' , context={'form' : form , 'todos' : todos})


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("show_todo")
        else: 
            return render(request , 'todo/addtodo.html' , context={'form' : form})


def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('show_todo')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('show_todo')