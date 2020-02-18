from .models import Serverlist
from django import forms

class ServerlistForm(forms.ModelForm):
    class Meta:
        model = Serverlist
        fields = ('name','team','server_count','model_name','code','use_case')
