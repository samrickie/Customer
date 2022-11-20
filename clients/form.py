from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Button, ButtonHolder, Submit, Layout
from django.forms.models import ModelForm
from django import forms
from django.urls import reverse

from clients.models import Users

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]


class UserCreateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'value': 'first name'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = FormHelper()

        helper.form_id = 'registration'
        helper.form_class = 'Registration'
        helper.use_custom_control = True
        helper.form_tag = True
        helper.form_method = 'POST'
        helper.form_action = reverse('register')

        helper.layout = Layout(
            Row(
                Div(
                    'first_name',
                    css_class='col-md-4'
                ),
                Div(
                    'last_name',
                    css_class='col-md-4'
                ),
                Div(
                    'phone',
                    css_class='col-md-4'
                ),

                Div(
                    'email',
                    css_class='col-md-4'
                ),
            ),

            Row(

                Div(
                    'age',
                    css_class='col-md-2'
                ),
                Div(
                    'gender',
                    css_class='col-md-2'
                ),
                Div(
                    'username',
                    css_class='col-md-2'
                ),
                Div(
                    'password',
                    css_class='col-md-2'
                )
            ),

            Submit('submit', 'SUBMIT', css_class='button white')
        )


