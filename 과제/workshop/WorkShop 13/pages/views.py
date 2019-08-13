from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def info(request):
    teacher = "Tak"
    students = ['박길동','김길동','홍길동']
    context = {
        'teacher' : teacher,
        'students' : students
    }
    return render(request, 'info.html',context)

def student(request,name):
    student = {'박길동':28, '김길동':26,'홍길동':10001230}
    context = {
        'name':name,
        'age':student[name]
    }
    return render(request, 'student.html', context)