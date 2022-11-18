
from django.urls import path
from registration_completed import views


app_name = "registration_completed"

urlpatterns = [
    path('registration_form/',views.registration_form, name="registration_form"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('edit/<int:id>/',views.edit, name="edit"),
]
