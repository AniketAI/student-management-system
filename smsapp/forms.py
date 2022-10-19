from django import forms 
from django.forms import Form, ModelForm
from smsapp.models import Courses, SessionYearModel, Semesters, TODO


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Semesters
    try:
        semesters_all = Semesters.objects.all()
        semesters_list = []
        for sem in semesters_all:
            sem_list= (sem.id, sem.semester)
            semesters_list.append(sem_list)
    except:
        semesters_list = []

    #For Displaying Semesters Classes
    try:
        semesters = Semesters.objects.all()
        semesters_sectionlist = []
        for sem in semesters:
            semsec_list = (sem.id, sem.section)
            semesters_sectionlist.append(semsec_list)
    except:
        semesters_sectionlist = []
    
    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []
    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    semesters_id = forms.ChoiceField(label="Semester", choices=semesters_list, widget=forms.Select(attrs={"class":"form-control"}))
    semesters_section_id = forms.ChoiceField(label="Section", choices=semesters_sectionlist, widget=forms.Select(attrs={"class":"form-control"}))
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Semesters
    try:
        semesters = Semesters.objects.all()
        semesters_list = []
        for sem in semesters:
            sem_list= (sem.id, sem.semesters)
            sem_list.append(sem_list)
    except:
        semesters_list = []
    
    
    #For Displaying Semesters Classes
    try:
        semesters = Semesters.objects.all()
        semesters_sectionlist = []
        for sem in semesters:
            semsec_list = (sem.id, sem.section)
            semsec_list.append(semsec_list)
    except:
        semesters_sectionlist = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    semesters_id = forms.ChoiceField(label="Semester", choices=semesters_list, widget=forms.Select(attrs={"class":"form-control"}))
    semesters_section_id = forms.ChoiceField(label="Section", choices=semesters_sectionlist, widget=forms.Select(attrs={"class":"form-control"}))
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))






class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority']