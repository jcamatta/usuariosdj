from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        min_length=6, 
        label='Password', 
        required=True, 
        widget=forms.PasswordInput(attrs=dict(plassholder='password')))
    
    repeated_password = forms.CharField(
        min_length=6, 
        label='Repeat Password',
        required=True, 
        widget=forms.PasswordInput(attrs=dict(plassholder='repeat password')))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'nombre', 'apellido', 'genero']

    def clean_repeated_password(self):
        password = self.cleaned_data.get('password')
        repeated_password = self.cleaned_data.get('repeated_password')
        print(password)
        print(repeated_password)
        if password != repeated_password:
            self.add_error('repeated_password', 'Las contraseñas no coinciden.')

    def clean_username(self):
        # Obtener el valor del campo username
        username = self.cleaned_data.get('username')

        # Verificar si ya existe un usuario con el mismo username
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya está en uso')

        return username