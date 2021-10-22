from allauth.account.forms import ChangePasswordForm
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from bugtail.helpers import form_helper
from accounts import forms
# Create your views here.

class SettingsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'add_email_form':form_helper._AddEmailForm(),
            'change_password_form':form_helper._ChangePasswordForm(),
            'profile_form':forms.ProfileForm(instance=self.request.user.profile),
            'user_form': forms.UserForm(instance=self.request.user),
        }
        return render(request, 'settings.html', context)
    

class ChangeUserDetailsView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(request.POST,instance=self.request.user)
        profile_form = forms.ProfileForm(request.POST,instance=self.request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account Updated Successfully 😜')
        else:
            messages.success(request, 'Error Occurred')
        return redirect('accounts:settings') 