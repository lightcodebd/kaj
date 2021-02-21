from django.urls import path

from . import views


urlpatterns = [

    path("", views.kaj_index, name="kaj_index"),
    path("<education_qualification>/", views.kaj_findbyqualification, name="kaj_findbyqualification"),
    path("<int:pk>/", views.kaj_detail, name="kaj_detail"),

]
