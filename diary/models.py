from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import models
from random import randint
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField

class Writer(AbstractUser):
    country = CountryField(blank_label='(select country)', default = 'CA')

    def __str__(self):
        return self.username

class EntryManager(models.Manager):
    def get_random_entry(self, user):
        '''
            returns a random entry that is not by the indicated user
        '''
        while True:
            numEntries= Entry.objects.all().count()
            random_index = randint(0, numEntries - 1)
            if (self.all()[random_index].writer != user):
                break

        return self.all()[random_index]

class Entry(models.Model):
    contents = RichTextField()
    pub_date = models.DateTimeField("Date Written", default = now)
    essential = models.BooleanField(default = False)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    objects = EntryManager()

    def __str__(self):
        return self.contents
