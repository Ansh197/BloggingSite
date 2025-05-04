from django import forms
from core.models import UserProfileModel

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ['portfolioSite','profilePic']
    