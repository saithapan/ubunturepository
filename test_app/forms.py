from django import forms
from .models import user_profile,customer_profile

class profile_Form(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = [
            'fname',
            'lname',
            'technology',
            'email',
            'display_picture'
        ]


class customer_profile_Form(forms.ModelForm):
    class Meta:
        model = customer_profile
        fields = [
            'c_name',
            'c_address',
            'c_file',
            'c_email',
            
        ]