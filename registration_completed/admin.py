from django.contrib import admin
from registration_completed.models import Form

# Register your models here.
class AdminForm(admin.ModelAdmin):
    list_display=("id","first_name","last_name","date_of_birth","gender","degree","email","number","description")


admin.site.register(Form,AdminForm)