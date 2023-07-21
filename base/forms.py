from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta: # two fields required always
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

