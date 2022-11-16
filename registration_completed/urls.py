
from django.urls import path
from registration_completed import views


app_name = "registration_completed"

urlpatterns = [
    path('registration_form/',views.registration_form, name="registration_form"),
]
