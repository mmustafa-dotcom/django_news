
import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Person, Student


def read_json(request):
    try:
        data = json.loads(request.body or "{}")

        if not isinstance(data, dict):
            return None

        return data

    except (json.JSONDecodeError, UnicodeDecodeError):
        return None


def serialize(obj):
    return {
        "id": obj.id,
        "firstname": obj.firstname,
        "lastname": obj.lastname,
        "age": obj.age
    }


def validate_data(data, partial=False):
    if data is None:
        return False

    allowed = {"firstname", "lastname", "age"}

    if not data or not set(data).issubset(allowed):
        return False

    if not partial and not allowed.issubset(data):
        return False

    for field in ("firstname", "lastname"):
        if field in data and not isinstance(data[field], str):
            return False

    if "age" in data:
        if isinstance(data["age"], bool) or not isinstance(data["age"], int):
            return False

    return True


def update_object(obj, data):
    for field in ("firstname", "lastname", "age"):
        if field in data:
            setattr(obj, field, data[field])

    obj.save()

    return obj


# =================================
# PEOPLE API
# =================================

# GET
def people_get(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET only"}, status=405)

    people = Person.objects.all()

    return JsonResponse(
        [serialize(person) for person in people],
        safe=False
    )


# POST
@csrf_exempt
def people_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = read_json(request)

    if not validate_data(data):
        return JsonResponse({"error": "Invalid data"}, status=400)

    person = Person.objects.create(
        firstname=data["firstname"],
        lastname=data["lastname"],
        age=data["age"]
    )

    return JsonResponse(serialize(person), status=201)


# PUT
@csrf_exempt
def person_update(request, pk):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT only"}, status=405)

    data = read_json(request)

    if not validate_data(data):
        return JsonResponse({"error": "Invalid data"}, status=400)

    person = get_object_or_404(Person, id=pk)

    update_object(person, data)

    return JsonResponse(serialize(person))


# PATCH
@csrf_exempt
def person_change(request, pk):
    if request.method != "PATCH":
        return JsonResponse({"error": "PATCH only"}, status=405)

    data = read_json(request)

    if not validate_data(data, partial=True):
        return JsonResponse({"error": "Invalid data"}, status=400)

    person = get_object_or_404(Person, id=pk)

    update_object(person, data)

    return JsonResponse(serialize(person))


# DELETE
@csrf_exempt
def person_delete(request, pk):
    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE only"}, status=405)

    person = get_object_or_404(Person, id=pk)
    person.delete()

    return JsonResponse({
        "message": "Person deleted successfully"
    })


# =================================
# STUDENT API
# =================================

# GET
def Student_list(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET only"}, status=405)

    students = Student.objects.all()

    return JsonResponse(
        [serialize(student) for student in students],
        safe=False
    )


# POST
@csrf_exempt
def Student_create(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = read_json(request)

    if not validate_data(data):
        return JsonResponse({"error": "Invalid data"}, status=400)

    student = Student.objects.create(
        firstname=data["firstname"],
        lastname=data["lastname"],
        age=data["age"]
    )

    return JsonResponse(serialize(student), status=201)


# PUT
@csrf_exempt
def Student_update(request, pk):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT only"}, status=405)

    data = read_json(request)

    if not validate_data(data):
        return JsonResponse({"error": "Invalid data"}, status=400)

    student = get_object_or_404(Student, id=pk)

    update_object(student, data)

    return JsonResponse(serialize(student))


# PATCH
@csrf_exempt
def Student_change(request, pk):
    if request.method != "PATCH":
        return JsonResponse({"error": "PATCH only"}, status=405)

    data = read_json(request)

    if not validate_data(data, partial=True):
        return JsonResponse({"error": "Invalid data"}, status=400)

    student = get_object_or_404(Student, id=pk)

    update_object(student, data)

    return JsonResponse(serialize(student))


# DELETE
@csrf_exempt
def Student_delete(request, pk):
    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE only"}, status=405)

    student = get_object_or_404(Student, id=pk)
    student.delete()

    return JsonResponse({
        "message": "Student deleted successfully"
    })
