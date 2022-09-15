from django import forms
from app1.models import LoginForm,VerifyDocument, feedback

CATEGORIES = (  
    ('G','Gender'),
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Other"),
)

class LoginField(forms.ModelForm):
    class Meta:
        model = LoginForm
        fields = '__all__'

class VerifyDocumentForm(forms.Form):
    
    Doc_No = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','id':'docno','placeholder':'Document Number', 'autofocus':'autofocus','required': True}))
    Front_image = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control','id':'front_image','name':'front_image','autofocus':'autofocus'}))
    Back_image = forms.ImageField(widget = forms.FileInput(attrs={'class':'form-control','id':'back_image','name':'back_image','autofocus':'autofocus'}))
    
class RegistrationForm(forms.ModelForm):
        class Meta:
            model = LoginForm
            fields = ['username','dob','gender','mobile','email','password','hint']

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name','email','message']
        