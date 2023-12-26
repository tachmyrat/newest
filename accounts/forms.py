from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
#forms py bu biz registrasiyta edilende jangonun tayyn bregistrasiyasyndan peydalanman oz islegimiz boyunca yasamaklyk ucin bolup duryar
# ilki bilen modelsde class doredip ony hem djangonun abstractuser diyen librarysyndan peydalanyp yasayas
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name','last_name','email','age','address',) #egerde biz bu yere bashgada bir zat goshjak bolsak mysal ucin tel nomeri onda biz ilki modells.pydaki class myza girizip sonra munba hem girizmeli
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','email','age','address',) #egerde biz bu verden username ya-da bashga bir zady ocursek shony hem uytgedip bolmaz yaly bolyar
        # admin.py registrasiya edyas hem-de birikdiryas