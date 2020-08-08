from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm 

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'user'
    slug_field = 'username'



    
    