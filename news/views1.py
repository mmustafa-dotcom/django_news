
from django.shortcuts import render, get_object_or_404

from .models import User, Person, Student


def users(request):
    data = User.objects.all()

    return render(
        request,
        "users.html",
        {"data1": data}
    )


def details1(request, id1):
    data = get_object_or_404(User, id=id1)

    return render(
        request,
        "details1.html",
        {"data": data}
    )


def people_page(request):
    people1 = Person.objects.all()

    return render(
        request,
        "people.html",
        {"people": people1}
    )


def students_page(request):
    students1 = Student.objects.all()

    return render(
        request,
        "students.html",
        {"students": students1}
    )
