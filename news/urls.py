from django.urls import path
from .views import home, details
from .views1 import users, details1, people_page, students_page
from . import api_views


urlpatterns = [
    path("home/", home),
    path("home/<int:id>/", details),

    path("users/", users),
    path("users/<int:id1>/", details1),

    path("people/", people_page),
    path("students/", students_page),

    # GET
    path("api/people/", api_views.people_get),

    # POST
    path("api/people/create/", api_views.people_api),

    # PUT
    path("api/people/<int:id>/", api_views.person_update),

    # DELETE
    path("api/people/<int:id1>/delete/", api_views.person_delete),

    # PATCH
    path("api/people/<int:id3>/change/", api_views.person_change),

    # GET
    path("api/students/", api_views.Student_list),

    path("api/students/", api_views.Student_list),
    path("api/students/create/", api_views.Student_create),
    path("api/students/<int:id11>/", api_views.Student_update),
    path("api/students/<int:id12>/change/", api_views.Student_change),
    path("api/students/<int:id14>/delete/", api_views.Student_delete),
]