from django.urls import path
from . import views, HodViews, AdminViews, StaffViews, StudentViews



urlpatterns = [
    # path('', views.index),
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout_user/', views.logout_user, name="logout_user"),


    # For Admin
    path('adminmain_home/', AdminViews.adminmain_home, name="adminmain_home"),
    path('show_admin_data/', AdminViews.show_admin_data, name="show_admin_data"),
    path('show_semester_data/', AdminViews.show_semester_data, name="show_semester_data"),
    path('add_hod/', AdminViews.add_hod, name="add_hod"),
    path('add_hod_save/', AdminViews.add_hod_save, name="add_hod_save"),
    path('add_mainstaff/', AdminViews.add_mainstaff, name="add_mainstaff"),
    path('add_mainstaff_save/', AdminViews.add_mainstaff_save, name="add_mainstaff_save"),
    path('add_mainstudent/', AdminViews.add_mainstudent, name="add_mainstudent"),
    path('add_mainstudent_save/', AdminViews.add_mainstudent_save, name="add_mainstudent_save"),
    path('add_maincourse/', AdminViews.add_maincourse, name="add_maincourse"),
    path('add_maincourse_save/', AdminViews.add_maincourse_save, name="add_maincourse_save"),
    path('add_mainsemester/', AdminViews.add_mainsemester, name="add_mainsemester"),
    path('add_mainsemester_save/', AdminViews.add_mainsemester_save, name="add_mainsemester_save"),
    path('delete/<str:id>/', AdminViews.delete, name="delete"),
    path('maindelete/<str:id>/', AdminViews.maindelete, name="maindelete"),
    path('add_session/', AdminViews.add_session, name="add_session"),
    path('add_session_save/', AdminViews.add_session_save, name="add_session_save"),


    # For HOD
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('add_course/', HodViews.add_course, name="add_course"),
    path('add_course_save/', HodViews.add_course_save, name="add_course_save"),
    


    # For Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),


    # For Students
    path('student_home/', StudentViews.student_home, name="student_home"),




    # For todo
   path('show_todo/' , AdminViews.show_todo, name="show_todo" ), 
   path('add-todo/' , AdminViews.add_todo, name="addtodo" ), 
   path('delete-todo/<int:id>' , AdminViews.delete_todo, name="delete_todo"), 
   path('change-status/<int:id>/<str:status>' , AdminViews.change_todo, name="change_todo" ),
]
