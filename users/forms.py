from django import forms
from .models import UserProfile 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio')
        # exclude =('user') user hariç hepsi demek.

class UserForm(UserCreationForm): #kullanıcı kaydolurken email de girmesini iatiyoruz o yüzden 
    #views deki def register i yoruma aldık .  override ettik 
    
    class Meta:
        model = User
        fields = ('username','email')
