from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','first_name','last_name','age','address','is_staff'] #biz bu yere admin panelde gorkezil;meli zatlaryn sanawuny yazdyk
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
#egerde biz shu registeri goshmasak registrasiya edenler admin panelda gorunmeyar
#indi bolsa appmizi makemigration we migrate komandalar bn migrat edyas we supper user doredelin