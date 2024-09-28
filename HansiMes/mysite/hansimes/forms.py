from django import forms
from hansimes.models import ContactMess, User
from django.contrib.auth.forms import AuthenticationForm

class ContactMessForm(forms.ModelForm):
    class Meta:
        model = ContactMess
        fields = ['Name', 'Email', 'Message']
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your name'}),
            'Email' : forms.EmailInput(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your email'}),
            'Message' : forms.Textarea(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your message', 'rows':5, 'cols':60})
        }
        labels = {
            'Name': 'Name',
            'Email': 'Email',
            'Message': 'Message'
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your username'}),
            'email' : forms.EmailInput(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your email'}),
            'password' : forms.PasswordInput(attrs={'class':'contact_us_form_input', 'placeholder':'Enter your password'})
        }
        labels = {
            'username':'Username',
            'email':'Email',
            'password':'Password'
        }        

class UserLoginForm(AuthenticationForm):
     username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'contact_us_form_input',
            'placeholder': 'Enter your username'
        })
    )
     password = forms.CharField(
         label="Password",
         widget=forms.PasswordInput(attrs={
             'class': 'contact_us_form_input',
             'placeholder': 'Enter your password'
         })
     )