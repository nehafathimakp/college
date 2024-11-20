from django.contrib import admin
from django.urls import path
from collegeapp import views

urlpatterns = [
    path('dep_add',views.dep_add,name='dep_add'),
    path('index',views.index,name='index'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('',views.mainhome,name='mainhome'),
    path('viewstudent',views.viewstudent,name="viewstudent"),
    path("approve/<int:aid>",views.approve,name='approve'),
    path('logins',views.logins,name='logins'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path("teacherhome",views.teacherhome,name='techerhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    # update student
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    # update teacher
    path('updatetr',views.updatetr,name='updatetr'),
    path('updateteacher/<int:utid>',views.updateteacher,name='updateteacher'),
    # view teacher
    path('viewteacher',views.viewteacher,name='viewteacher'),
    # delete teacher
    path('deletetr/<int:dtid>',views.deletetr,name='deletetr'),
    #delete student
    path('deletestud/<int:dsid>',views.deletestud,name='deletestud'), 
    #logout 
    path('lgout',views.lgout,name='lgout')
 ]