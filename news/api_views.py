import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scipy.sparse import data

from .models import Person, Student


@csrf_exempt
def people_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        person = Person.objects.create(
            firstname=data["firstname"],
            lastname=data["lastname"],
            age=data["age"]
        )

        return JsonResponse({
            "id": person.id,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "age": person.age
        })

    return JsonResponse({
        "error": "Only POST is allowed"
    })


@csrf_exempt
def person_update(request,id):
    if request.method == "PUT":

        data = json.loads(request.body)

        person = Person.objects.get(id=id)

        person.firstname = data["firstname"]
        person.lastname = data["lastname"]
        person.age = data["age"]

        person.save()

        return JsonResponse({
            "id": person.id,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "age": person.age
        })

    return JsonResponse({})

@csrf_exempt
def person_delete(request, id1):
    if request.method == "DELETE":
        person = Person.objects.get(id=id1)
        person.delete()

        return JsonResponse({})
    return JsonResponse({})

@csrf_exempt
def person_change(request,id3):
    if request.method == "PATCH":
        data = json.loads(request.body)
        person = Person.objects.get(id=id3)
        person.firstname = data["firstname"]
        person.lastname = data["lastname"]
        person.age = data["age"]
        person.save()
        return JsonResponse({})

@csrf_exempt
def people_get(request):
    if request.method == "GET":
        people = Person.objects.all()

        data = []

        for person in people:
            data.append({
                "id": person.id,
                "firstname": person.firstname,
                "lastname": person.lastname,
                "age": person.age
            })

        return JsonResponse(data, safe=False)













# GET_Student
@csrf_exempt
def Student_list(request):
    if request.method == "GET":
        a = Student.objects.all()
        data = []

        for person in a:
            data.append({
                "id": person.id,
                "firstname": person.firstname,
                "lastname": person.lastname,
                "age": person.age
            })

        return JsonResponse(data, safe=False)


# POST
@csrf_exempt
def Student_create(request):
    if request.method == "POST":

        data = json.loads(request.body)

        person = Student.objects.create(
            firstname=data["firstname"],
            lastname=data["lastname"],
            age=data["age"]
        )

        return JsonResponse({
            "id": person.id,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "age": person.age
        })

    return JsonResponse({
        "error": "Only POST is allowed"
    })


# PUT
@csrf_exempt
def Student_update(request, id11):
    if request.method == "PUT":

        data = json.loads(request.body)

        person = Student.objects.get(id=id11)

        person.firstname = data["firstname"]
        person.lastname = data["lastname"]
        person.age = data["age"]

        person.save()

        return JsonResponse({
            "id": person.id,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "age": person.age
        })

    return JsonResponse({})


# PATCH
@csrf_exempt
def Student_change(request, id12):
    if request.method == "PATCH":

        data = json.loads(request.body)

        person = Student.objects.get(id=id12)

        person.firstname = data["firstname"]
        person.lastname = data["lastname"]
        person.age = data["age"]

        person.save()

        return JsonResponse({
            "id": person.id,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "age": person.age
        })

    return JsonResponse({})


# DELETE
@csrf_exempt
def Student_delete(request, id14):
    if request.method=="DELETE":
        person=Student.objects.get(id=id14)
        person.delete()

        return JsonResponse({})
    return JsonResponse({})


