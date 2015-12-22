from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.forms import widgets


class ContactForm(forms.Form):

    name = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            ),
            Fieldset('email', css_class='blockundso'),
        )

