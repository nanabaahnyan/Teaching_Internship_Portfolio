import os
from django.http import FileResponse, Http404, HttpResponse
from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'active_page': 'home'})


def cv(request):
    return render(request, 'cv.html', {'active_page': 'cv'})


def philosophy(request):
    return render(request, 'philosophy.html', {'active_page': 'philosophy'})


def scheme(request):
    return render(request, 'scheme.html', {'active_page': 'scheme'})


def lesson(request):
    return render(request, 'lesson.html', {'active_page': 'lesson'})


def assessment(request):
    return render(request, 'assessment.html', {'active_page': 'assessment'})


def tlm(request):
    return render(request, 'tlm.html', {'active_page': 'tlm'})


def reflective(request):
    return render(request, 'reflective.html', {'active_page': 'reflective'})


def mentor(request):
    return render(request, 'mentor.html', {'active_page': 'mentor'})


def gallery(request):
    return render(request, 'gallery.html', {'active_page': 'gallery'})

def quizzes(request):
    return render(request, 'quizzes.html', {'active_page': 'tlm'})

def assignments(request):
    return render(request, 'assignments.html', {'active_page': 'assessment'})

def exams(request):
    return render(request, 'exams.html', {'active_page': 'assessment'})

def exercises(request):
    return render(request, 'exercises.html', {'active_page': 'assessment'})

def projects(request):
    return render(request, 'projects.html', {'active_page': 'assessment'})

def preview_cv(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'EZEKIEL_BAAH_CV.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("CV not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="EZEKIEL_BAAH_CV.pdf"'
        return response
    
def preview_philosophy(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'Teaching_Philosophy.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Philosophy not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="Teaching_Philosophy.pdf"'
        return response
    
def preview_scheme_FORM1(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'FORM_1_Scheme_of_Work.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Scheme of Work not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="FORM_1_Scheme_of_Work.pdf"'
        return response
    
def preview_scheme_FORM2(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'FORM_2_Scheme_of_Work.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Scheme of Work not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="FORM_2_Scheme_of_Work.pdf"'
        return response
    
def preview_lesson_SHS1(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'LESSON_NOTE_FORM_1.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Lesson note not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="LESSON_NOTE_FORM_1.pdf"'
        return response
    
    
def preview_lesson_SHS2(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'LESSON_NOTE_FORM_2.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Lesson note not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="LESSON_NOTE_FORM_2.pdf"'
        return response
    
def preview_marking_SHS2(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'FORM_2_MARKING_SCHEME.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Marking scheme not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="FORM_2_MARKING_SCHEME.pdf"'
        return response
    
def preview_marking_SHS1(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'documents', 'FORM_1_MARKING_SCHEME.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("Marking scheme not found")
    
    with open(pdf_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="FORM_1_MARKING_SCHEME.pdf"'
        return response
    