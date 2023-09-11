from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.files.images import get_image_dimensions
from django import forms
from .models import UserProfile

class NewUserProfileForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class UpdateAvatarForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('avatar',)
    
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            width_avatar, height_avatar = get_image_dimensions(avatar)
            max_width = max_height = 900

            if width_avatar > max_width or height_avatar > max_height:
                raise forms.ValidationError(f'Use una imagen que tenga {max_width} x {max_height} pixeles o menos.')
            
            main, sub = avatar.content_type.split('/')
            if not(main == 'image' and sub in ['jpeg', 'png', 'gif']):
                raise forms.ValidationError('Por favor, usa imágenes JPEG, PNG, o GIF')
            
            if len(avatar) > (1024 * 1024):
                raise forms.ValidationError('El avatar no puede pesar mas de 20KB')
            
        except AttributeError:
            pass

        return avatar

class UpdateUserProfileForm(UpdateUserForm,UpdateAvatarForm):
    pass

##UserChangeForm para editar los campos(fields) de django
##ModelForm para crear formularios personalizados