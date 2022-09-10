from django.forms import ModelForm
from .models import Geek
  
# creating a form 
class GeeksForm(ModelForm):
    class Meta:
        model = Geek
        fields = "__all__"