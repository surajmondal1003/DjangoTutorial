from django import forms
from first_app.models import users_test
from django.core import validators
class Myform(forms.Form):
    name=forms.CharField(label='Name',
                        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    email=forms.EmailField(label='Email',
                        widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    verify_email=forms.EmailField(label="Enter Your Email Again",
                                  widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'on'}))
    text=forms.CharField(required=False,
                         widget=forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'on'}))

    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        v_email=all_clean_data['verify_email']

        if email != v_email :
            raise forms.ValidationError("Your emails did not match..")

class MyModelForm(forms.ModelForm):

    class Meta:
        model=users_test
        fields = '__all__'