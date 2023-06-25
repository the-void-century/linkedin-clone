from django import forms
from . models import User,JobPost

class LoginForm(forms.Form):
    username= forms.CharField(max_length=100)
    password= forms.CharField(label='Password',widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','first_name','last_name','email','profile_picture','wall']
    
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class UserEditForm(forms.ModelForm):

    class Meta:
        model= User
        fields=('first_name',
                'last_name','date_of_birth','profile_picture','wall','headline','summary'
                ,'location')
    
class JobPostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=('job_title','company_title','job_summary','apply_link','location')

# class ConnectionRequest(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=(User)