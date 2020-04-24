from django import forms
from request.models import Profile

class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ['url']