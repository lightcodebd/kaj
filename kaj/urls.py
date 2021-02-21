from django.urls import path

from . import views


urlpatterns = [

    path("", views.kaj_index, name="kaj_index"),
    path("<jobtitle>/", views.kaj_detail, name="kaj_detail"),
#    path("<pk>/", views.project_detail, name="project_detail"),

]
