from django.forms import ModelForm

from .models import Note


class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text',]
