from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from .models import Writer, Entry
from ckeditor.widgets import CKEditorWidget
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class writerCreationForm(UserCreationForm): # 'writer' is the name of the custom user class

    class Meta(UserCreationForm):
        model = Writer
        fields = ('username', 'email', 'first_name', 'last_name', 'country')
        country = CountryField().formfield()
        widgets = {'country': CountrySelectWidget()}

class writerChangeForm(UserChangeForm):
    # username = forms.CharField(initial = username)

    class Meta:
        model = Writer
        fields = ('email', 'first_name', 'last_name', 'country')
        country = CountryField().formfield()
        widgets = {'country': CountrySelectWidget()}

class changePasswordForm(PasswordChangeForm):

    class Meta:
        model = Writer

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['contents',]
        labels = {
            'contents' : _(""),
        }
        # widgets = {
        #     'contents' : Textarea(attrs={'cols' : 120, 'rows' : 30}),
        # }
