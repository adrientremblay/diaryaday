from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import writerCreationForm, writerChangeForm
from .models import Writer
from .models import Entry

class WriterAdmin(UserAdmin):
    add_form = writerCreationForm
    form = writerChangeForm
    model = Writer
    list_display = ['email', 'username',]

admin.site.register(Writer)
admin.site.register(Entry)
