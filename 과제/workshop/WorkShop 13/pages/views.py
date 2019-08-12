from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def student(request,name):
    student = {'박길동':28, '김길동':26,'홍길동':10001230}
    context = {
        'name':name,
        'age':student[name]
    }
    return render(request, 'student.html', context)