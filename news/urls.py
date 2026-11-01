
from django.urls import path

from . import views, views1, api_views


urlpatterns = [

    # NEWS
    path("", views.home, name="home"),
    path("home/", views.home, name="home_page"),
    path("home/<int:id>/", views.details, name="details"),

    # USERS
    path("users/", views1.users, name="users"),
    path("users/<int:id1>/", views1.details1, name="details1"),

    # PEOPLE AND STUDENTS HTML
    path("people/", views1.people_page, name="people"),
    path("students/", views1.students_page, name="students"),

    # PEOPLE API
    path("api/people/", api_views.people_get, name="people_get"),
    path("api/people/create/", api_views.people_api, name="people_create"),
    path("api/people/<int:pk>/", api_views.person_update, name="person_update"),
    path("api/people/<int:pk>/change/", api_views.person_change, name="person_change"),
    path("api/people/<int:pk>/delete/", api_views.person_delete, name="person_delete"),

    # STUDENTS API
    path("api/students/", api_views.Student_list, name="student_list"),
    path("api/students/create/", api_views.Student_create, name="student_create"),
    path("api/students/<int:pk>/", api_views.Student_update, name="student_update"),
    path("api/students/<int:pk>/change/", api_views.Student_change, name="student_change"),
    path("api/students/<int:pk>/delete/", api_views.Student_delete, name="student_delete"),
]
