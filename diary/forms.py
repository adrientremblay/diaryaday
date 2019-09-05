from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, ReadOnlyPasswordHashField
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from .models import Writer, Entry
from ckeditor.widgets import CKEditorWidget
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class writerCreationForm(UserCreationForm): # 'writer' is the name of the custom user class

    name = forms.CharField(
        max_length=100,
        label=_("First Name"),
        help_text=_(
            "<ul>"
            "<li>Entering a name is NOT required. (name will be displayed with your diary entries when given)</li>"
            "</ul>"
        ),
        required=False,
    )

    class Meta(UserCreationForm):
        model = Writer
        fields = ('username', 'name', 'country')
        widgets = {'country': CountrySelectWidget()}

class writerChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see your "
            "password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        )
    )

    class Meta:
        model = Writer
        fields = ('name', 'country')
        widgets = {'country': CountrySelectWidget()}

class changePasswordForm(PasswordChangeForm):

    class Meta:
        model = Writer

class MyReadOnlyPasswordHashWidget(forms.Widget):
    template_name = 'auth/widgets/read_only_password_hash.html'
    read_only = True

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        summary = []
        if not value or value.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary.append({'label': gettext("No password set.")})
        else:
            try:
                hasher = identify_hasher(value)
            except ValueError:
                summary.append({'label': gettext("Invalid password format or unknown hashing algorithm.")})
            else:
                for key, value_ in hasher.safe_summary(value).items():
                    summary.append({'label': gettext(key), 'value': value_})
        context['summary'] = summary
        return context

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
