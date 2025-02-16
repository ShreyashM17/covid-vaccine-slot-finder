from django import forms
from django.forms import ModelForm
from .models import Registrations


class SignupForm(ModelForm):
    Date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'fields'
    }))
    Phone_number = forms.IntegerField(widget=forms.TextInput(attrs=
                                                      {
                                                          "maxlength": "10",
                                                          "minlength": "10",
                                                          "class": 'fields',
                                                      }))
    Email_id = forms.EmailField(widget=forms.TextInput(attrs=
                                                       {
                                                           "class": 'fields',
                                                           "type": "email",
                                                       }))
    First_name = forms.CharField(widget=forms.TextInput(attrs={
                                                            'class': 'fields'
                                                            }))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={
                                                            'class': 'fields'
                                                            }))
    #Document = forms.CharField(widget=forms.TextInput(attrs={
                                                            #'class': 'fields'
                                                            #}))
    document_no = forms.CharField(widget=forms.TextInput(attrs={
                                                            'class': 'fields'
                                                            }))

    class Meta:
        model = Registrations
        fields = [
            'Email_id',
            'First_name',
            'Last_name',
            'Phone_number',
            'Date_of_birth',
            'Document',
            'document_no',
        ]

    def clean_data(self):
        data = {
            'email_id': self.cleaned_data['Email_id'],
            'first_name': self.cleaned_data['First_name'],
            'last_name': self.cleaned_data['Last_name'],
            'phone_number': self.cleaned_data['Phone_number'],
            'dob': self.cleaned_data['Date_of_birth'],
            'document': self.cleaned_data['Document'],
            'doc_no': self.cleaned_data['document_no'],
        }
        return data


class PasswordForm(ModelForm):
    Password = forms.CharField(widget=forms.TextInput(attrs=
                                                      {
                                                          "type": "password",
                                                          "id": "newpass",
                                                          "maxlength": "12",
                                                          "minlength": "8",
                                                      }))

    class Meta:
        model = Registrations
        fields = [
            'Password'
        ]


class Login(ModelForm):
    Password = forms.CharField(widget=forms.TextInput(attrs=
                                            {
                                                "type": "password",
                                                "maxlength": "12",
                                                "minlength": "8",
                                                "id": "mypass",
                                                'class': "form-control",
                                                'name': "password",
                                                'placeholder': "Password",
                                            }))

    Email_id = forms.CharField(widget=forms.TextInput(attrs={
                                    'class': "form-control",
                                    'type': "email",
                                    'name': "email",
                                    'placeholder': "Email",
                                }))

    class Meta:
        model = Registrations
        fields = [
            'Email_id',
            'Password'
        ]
