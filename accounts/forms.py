from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from articles.models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  # Customize fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control'})  # Add CSS class

    def clean_body(self):
        body = self.cleaned_data['comment']
        # Add validation logic here, e.g., for spam detection, length restrictions, etc.
        return body

#forms py bu biz registrasiyta edilende jangonun tayyn bregistrasiyasyndan peydalanman oz islegimiz boyunca yasamaklyk ucin bolup duryar
# ilki bilen modelsde class doredip ony hem djangonun abstractuser diyen librarysyndan peydalanyp yasayas
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'profile_picture','first_name','last_name','email','age','address',) #egerde biz bu yere bashgada bir zat goshjak bolsak mysal ucin tel nomeri onda biz ilki modells.pydaki class myza girizip sonra munba hem girizmeli
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','email','age','address','profile_picture') #egerde biz bu verden username ya-da bashga bir zady ocursek shony hem uytgedip bolmaz yaly bolyar
        # admin.py registrasiya edyas hem-de birikdiryas
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'address', 'profile_picture')  # Adjust fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False  # Make profile picture optional