from django.urls import reverse_lazy

ACCOUNT_AUTHENTICATION_METHOD = ['username', 'email', 'username_email'][1]
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION  = ['madatory', 'optional', 'none'][1]
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS  = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300 #In seconds
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL  = reverse_lazy('accounts:settings')
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_FORMS = {
    'add_email': 'bugtail.helpers.form_helper._AddEmailForm',
    'login': 'bugtail.helpers.form_helper._LoginForm',
    'signup': 'bugtail.helpers.form_helper._SignupForm',
    'reset_password' : 'bugtail.helpers.form_helper._ResetPasswordForm',
    'change_password' : 'bugtail.helpers.form_helper._ChangePasswordForm',
    'reset_password_from_key': 'bugtail.helpers.form_helper._ResetPasswordFromKeyForm',
}