from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from .models import CustomUser
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import CustomUserCreationForm ,CustomUserChangeForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name='registration/signup.html'

class ProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser  # Specify the model to use for the list
    template_name = 'registration/profil.html' 
    def test_func(self):
        # profile_url = reverse('profile', kwargs={'pk': self.request.user.id})
        return self.request.user.id == self.kwargs['pk']  # Assuming you're using PK for comparison
class ChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/change.html'
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id})
    def test_func(self):
        # profile_url = reverse('profile', kwargs={'pk': self.request.user.id})
        return self.request.user.id == self.kwargs['pk'] 