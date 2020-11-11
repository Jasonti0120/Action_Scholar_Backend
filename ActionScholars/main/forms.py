from django.forms import ModelForm
from .models import *

class AddHourForm(ModelForm):
    class Meta:
        model = Event_Student
        fields = ['student','Event','Student_Reflection']
