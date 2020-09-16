from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:##Meta is use to create field on form
        model=Todo
        fields=['title','memo','important']

