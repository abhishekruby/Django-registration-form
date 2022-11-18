from django import forms
from registration_completed.models import Form
from registration_completed.models import GENDER_CHOICES,DEGREE_CHOICES



class RegistrationForm(forms.ModelForm):
    gender = forms.RadioSelect(choices=GENDER_CHOICES)
    degree = forms.ChoiceField(choices=DEGREE_CHOICES)
    class Meta:
        model = Form
        fields = '__all__' 
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "gender": forms.RadioSelect(attrs={'class': ""}),
            "degree": forms.Select(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "description": forms.Textarea(attrs={'class': "form-control"}),
        }
