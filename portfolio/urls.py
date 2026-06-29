from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.cv, name='cv'),
    path('cv/preview/', views.preview_cv, name='cv_preview'),
    path('philosophy/', views.philosophy, name='philosophy'),
    path('philosophy/preview/', views.preview_philosophy, name='philosophy_preview'),
    path('scheme/', views.scheme, name='scheme'),
    path('scheme/preview/FORM1/', views.preview_scheme_FORM1, name='scheme_preview_FORM1'),
    path('scheme/preview/FORM2/', views.preview_scheme_FORM2, name='scheme_preview_FORM2'),
    path('lesson/', views.lesson, name='lesson'),
    path('lesson/preview/SHS1/', views.preview_lesson_SHS1, name='lesson_preview_SHS1'),
    path('lesson/preview/SHS2/', views.preview_lesson_SHS2, name='lesson_preview_SHS2'),
    path('assessment/', views.assessment, name='assessment'),
    path('assessment/preview/SHS1/', views.preview_marking_SHS1, name='assessment_preview_SHS1'),
    path('assessment/preview/SHS2/', views.preview_marking_SHS2, name='assessment_preview_SHS2'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('tlm/', views.tlm, name='tlm'),
    path('reflective/', views.reflective, name='reflective'),
    path('mentor/', views.mentor, name='mentor'),
    path('gallery/', views.gallery, name='gallery'),
    path('assignments/', views.assignments, name='assignments'),
    path('exams/', views.exams, name='exams'),
    path('exercises/', views.exercises, name='exercises'),
    path('projects/', views.projects, name='projects'),
]
