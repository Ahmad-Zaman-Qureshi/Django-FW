from django.shortcuts import render, redirect
from .forms import StForm, BkForm, BIssueForm
from .models import Students, Book, Book_Issue

def index(request):
    return(render(request, 'index.html'))

def Student(request):
    form = StudentsForm
    return (render(request, 'student.html', {'form':form}))

def Book(request):
    form = BookForm
    return (render(request, 'book.html', {'form':form}))

def B_Issue(request):
    form = Book_IssueForm
    return (render(request, 'b_issue.html', {'form':form}))

def S_Form(request):
    form = StForm(request.POST)
    form.save()
    return redirect('S_Form')

def B_Form(request):
    form = BkForm(request.POST)
    form.save()
    return redirect('BkForm')
def R_Form(request):
    form = BIssueForm(request.POST)
    form.save()
    return redirect('BIssueForm')

def view_student(request):
    stud = Students.objects.order_by('-id')
    return render(request,'VStudents', {'stud': stud})

def view_book(request):
    bk = Book.objects.order_by('-id')
    return render(request,'view_b.html', {'bk': bk})

def view_book_issue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'view_bissue.html', {'issue': issue})