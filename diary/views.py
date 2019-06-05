from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views

from .forms import writerCreationForm, writerChangeForm, changePasswordForm, EntryForm
from .models import Entry, Writer
from datetime import datetime

class SignUp(generic.CreateView):
    form_class = writerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(SuccessMessageMixin, generic.UpdateView):
    model = Writer
    form_class = writerChangeForm
    template_name = 'diary/profile.html'
    success_url = '/diary/'
    success_message = "Your Profile Has Been Updated!"

    def get_initial(self):
        # get_initial should return dict. They should be rendered in template.
        writer = Writer.objects.get(pk=1) # first get data from database.
        # dictionary key names should be same as they are in forms.
        return {
            'username': writer.username,
            'email': writer.email,
            'first_name': writer.first_name,
            'last_name' : writer.last_name
        }

    def get_object(self):
        return get_object_or_404(Writer, pk=self.request.user.id)


class IndexView(TemplateView):
    template_name = "diary/index.html"

class WriteView(CreateView):
    template_name = 'diary/write.html'
    form_class = EntryForm
    success_url = '/diary/read'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.writer.save()
        self.request.session['write_success'] = True

        return super().form_valid(form)

class ReadView(TemplateView):
    template_name = 'diary/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try :
            context['write_success'] = self.request.session['write_success']
        except:
            context['write_success'] = False
        context['entry'] = Entry.objects.get_random_entry(self.request.user)
        self.request.session['write_success'] = False
        return context

class ChangePasswordView(SuccessMessageMixin, auth_views.PasswordChangeView):
    form_class = changePasswordForm
    template_name = "password.html"
    success_url = '/diary/'
    success_message = "Password Changed Succesfully!"

    def get_form_kwargs(self):
            kwargs = FormMixin.get_initial(self)
            kwargs['user'] = self.request.user
            if self.request.method == 'POST':
                kwargs['data'] = self.request.POST
            return kwargs
