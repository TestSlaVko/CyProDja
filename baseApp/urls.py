from django.urls import path
from . import views

app_name = 'baseApp' 
urlpatterns = [
    path('',views.HomePg,name=''),
    path('page/',views.taskList,name='page'),
    path('login/',views.LoginPg,name='log'),
    path('register/',views.RegisterPg,name='register'),
    path('index/',views.IndexPg,name='index'),
    path('profile/',views.ProfilePg,name='profile'),
    path('courses/',views.CoursesPg,name='courses'),
    path('notes/',views.NotesPg,name='notes'),
    path('analytics/',views.AnalyticsPg,name='analytics'),
    path('certifications/',views.CertificationsPg,name='certifications'),
    path('findCourses/',views.FindCoursesPg,name='findCourses'),
    path('viewCourses/',views.ViewCoursesPg,name='viewCourses')
]