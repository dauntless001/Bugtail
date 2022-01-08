from django import forms
from accounts import models


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly':True}))
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['bio']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'bio':
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = '3'
            else:
                field.widget.attrs['class'] = 'form-control'