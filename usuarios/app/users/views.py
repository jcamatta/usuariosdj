from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegisterForm
# Create your views here.

class UserRegister(FormView):
    template_name = 'users/user_register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user_register')

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'], 
            form.cleaned_data['password'], 
            nombre=form.cleaned_data['nombre'], 
            apellido=form.cleaned_data['apellido'], 
            genero=form.cleaned_data['genero']
        )
        # agregar form.save() aqui seria un error ya que intentaria crear y 
        # guardar el mismo usuario dos veces lo cual crearia un error de integridad
        # Puede tener sentido si create_user almacena el usuario en una base de datos distinta
        return super().form_valid(form)