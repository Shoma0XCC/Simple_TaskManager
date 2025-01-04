from django.forms import ModelForm, TextInput,Select

from main.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'status']
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description'
            }),
            'status': Select(attrs={
                'class': 'form-control'
            })
        }
