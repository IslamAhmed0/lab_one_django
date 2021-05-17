from django.shortcuts import render,redirect
from  django.http import HttpResponse
from courses.models import Student,Track
# Create your views here.
# books = [{"name": "Php", "Author": "Ahmed", "details": "about php languages", "image": "one.jpeg", "id": "1"},
#          {"name": "Python", "Author": "Mohamed", "details": "about Python languages", "image": "two.jpg", "id": "2"},
#          {"name": "Networking", "Author": "Ibhrahim", "details": "about how to build a network with people",
#           "image": "one.jpg", "id": "3"},
#          {"name": "ITI", "Author": "Noura", "details": "life_in_iti", "image": "two.jpeg", "id": "4"}
#          ]
from courses.form import StudentModelForm,StudentForm


def show_all(req):

    student = Student.objects.all()
    # for book in books:
    context = {"students": student}
    return render(req, 'index.html', context)


def book (req, id):
    students = Student.objects.filter(id=id)

    context={"student":students[0]}
    return render (req, "book.html", context)

def delete(req, id):
    student= Student.objects.get(id=id)
    student.delete()
    return redirect('/courses')



def create(req):
    if req.method == 'GET':
      form =StudentModelForm()
      context={
          "form":form
      }
      return render(req,"create.html" ,context)
    elif req.method == 'POST':
        form=StudentModelForm(req.POST)
        form.save()
        # print(req)
        # student= Student()
        # student.fname = req.POST.get('fname')
        # student.lname = req.POST.get('lname')
        # student.age = req.POST.get('age')
        # student.track_id = req.POST.get('student_track')
        # student.save()

        return redirect('/courses')

def edit(req,id):
      st =Student.objects.get(id=id)
      form = StudentModelForm(instance= st)

      if req.method == 'POST':
          form = StudentModelForm(req.POST,instance= st)
          form.save()
          return redirect('/courses')

      context = {
            "form": form
     }
      return render(req, "create.html", context)

